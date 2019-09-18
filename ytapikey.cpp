#include<iostream>
#include<stdlib.h>


using namespace std;

int main(int argc, char* argv[]){
	if(argc>1){
		cout<<"KEY: "<<argv[1]<<endl;
		string k=string(argv[1]);
		system(("python3 -c \"import ytapikey; ytapikey.setkey('"+k+"')\"").c_str());
	}else{
		system("python3 -c \"import ytapikey; ytapikey.printkey()\"");
		//cout<<"\n";
	}
	return 0;
}
