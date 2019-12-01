#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <sstream>
#include <algorithm>

using namespace std;

//uma trans possui:
//uma string( estado de entrada)
//um caracter( letra do alfabeto)
//uma string( estado de saida) 
typedef struct
{
    string in;
    char letter;
    string out;
}trans;

//um af possui:
//um string(nome)
//um vetor de strings (estados do automato)
//um vetor de caracters(alfabeto de entrada)
//uma string (estado inicial)
//um vetor de strings (estados finais)
//um vetor de transicoes (transicoes)
typedef struct
{
    string name;//nome
    vector<string> states;//estados
    vector<char> alphabet;//alfabeto
    string ini; //estado inicial
    vector<string> fin; // estados finais
    vector<trans> t;// transicoes
}af;


//Functions
vector<string> parse(string line, char delim)
{
    stringstream subline(line);

    vector<string> v;
    string tmp;

    while(getline(subline, tmp, delim))
    {
        v.push_back(tmp);
    }

    return v;
}

void setStates(af &a, vector<string> tokens)
{
    //coloca os tokens nos estados do af
    for(int i = 0; i < tokens.size(); i ++)
        a.states.push_back(tokens[i]);
}

void setAlfa(af &a, vector<string> tokens)
{
    //coloca os tokens no alfabeto do af
    for(int i = 0; i < tokens.size(); i ++)
        a.alphabet.push_back(tokens[i][0]);
}

void setFin(af &a, vector<string> tokens)
{
    //coloca os tokens nos estados finais do af
    for(int i = 0; i < tokens.size(); i ++)
        a.fin.push_back(tokens[i]);
}

void setTrans(af &a, string line)
{
    stringstream subline(line);
    string qini;
    string letter;
    string qnext;

    trans t;

    subline.ignore(256,'('); // ignora o (
    getline(subline, qini, ',');// pega o estado inicial da transicao
    getline(subline, letter, ')');// pega o caracter da transicao
    subline.ignore(256, '='); //ignora o =
    getline(subline, qnext);// pega o caracter da transicao

    t.in = qini;
    t.letter =  letter[0];
    t.out = qnext;

    a.t.push_back(t);
}
af readAuto(string fileName)
{
    af a;

    string line; // uma linha do arquivo
    string pare; // sublinha dentro do parenteses

    string state;// string com os estados separados por virgula
    string alfabeto;// string com o alfabeto separado por virgula
    string finals; //string com os estados finais;

    vector<string> tokens;// atributos do automato


    ifstream file(fileName); // abrindo o arquivo


    if(file.is_open())
    {
        getline(file, line);
        //Primeira linha

        stringstream subline(line);

        getline(subline, a.name, '='); // pega o nome do automato
        subline.ignore();//pula o (
        subline.ignore();//pula o {

        getline(subline,state, '}');
        tokens = parse(state, ',');

        setStates(a, tokens); // coloca os estados o af

        subline.ignore(256, ',');//pula a , com ate 256 espacos
        subline.ignore(256, '{');//pula o { com ate 256 espacos

        getline(subline,alfabeto, '}');
        tokens = parse(alfabeto, ',');

        setAlfa(a, tokens);//coloca o alfabeto no af

        subline.ignore(256, ',');//pula a ,

        getline(subline,a.ini, ',');// pega o estado inicial

        subline.ignore(256, '{'); //pula o {

        getline(subline,finals, '}');
        tokens = parse(finals, ',');

        setFin(a, tokens); //coloca o conjunto finals no af


        while(getline(file,line) && line != "Prog"); //ignora o Prog

        while(getline(file,line))
        {
            setTrans(a, line);
        }

    }

    else cout << "[!] Nao consigui abrir o arquivo !!!\n";

    return a;
}

af afdForm(af afn)
{
    //Funcao que transforma um afn em afd
    //

    af afd;

    string current = afn.t[0].in; //estado atual da transicao, como esta ordenado
                                  //podemos apenas verificar quando muda esse estado

    cout << afn.ini;
    af afd.t.push_back(afn.ini);

    for(uint i = 0; i < afn.states.size(); i++)
    {
        for(uint j = 0; j < afn.alphabet.size();i ++)
        {


        }
    }

}

af autoMin(af afn)
{

}



bool sortbyTrans(trans a, trans b)
{
    return a.in < b.in;
}

void genGr(af afd)
{
    cout << "G = ({"; // nome da gramatica 

    for(uint i = 0; i < afd.states.size(); i++)
    {
        cout << afd.states[i];// Demais Variaveis

        if(i != afd.states.size() - 1)
        {
           cout <<  ","; // Nao poe virgula no ultimo
        }
    }

    cout << "},{";

    for(uint i = 0; i < afd.alphabet.size(); i++)
    {
        cout << afd.alphabet[i];

        if(i != afd.alphabet.size() - 1)
        {
            cout  << ",";
        }
    }

    cout << "},";

    cout << afd.ini << "," << "P)\n";

    cout << "P\n";



    string prod = afd.t[0].in;

    for(uint i = 0; i < afd.t.size(); i++)
    {
            cout << afd.t[i].in << " -> ";
            cout << afd.t[i].letter;
            cout << " " <<  afd.t[i].out << endl;
    }


}



