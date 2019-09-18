#include<iostream>
#include<stdlib.h>

using namespace std;

int main(int argc, char** argv){
	if(argc==1){
		system("python3 /home/daniele/Desktop/Code/YouTubeDownloader/yt.py");
	}else if(argc==2){
		system("ytapikey");
	}else if(argc==3){
		string cmd="ytapikey "+string(argv[2]);
		system(cmd.c_str());
	}
	return 0;
}
