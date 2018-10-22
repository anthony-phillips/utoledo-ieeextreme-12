#include<iostream>
#include<iomanip>
#include<tuple>
#include<map>
#include<fstream>
#define files 1
 
using namespace std;
   	 //as reference - how to access elements
   	 //cout <<"head at (" <<std::get<0>(std::get<0>(snakes[i])) <<',' <<std::get<1>(std::get<0>(snakes[i])) <<")\n";
    
int board_size;
class link{
public:    
    tuple<int, int> data;
    int type;
    link *node;
};
 
void append(link a, link* to_add)
{
    while (a.node!=NULL) a=*a.node;
    //cout <<get<0>(a.data) <<'\n';
}
 
void process(std::map<int, link> m, int d[], int d_size, int players)
{
    std::map<int, link>::iterator it;
    int tiles=board_size*board_size-1;
    int player_list[players];
    for (int i=0; i < players; ++i)
   	 player_list[i]=0;
    bool moved=false;
    for (int i=0; i < d_size; ++i)
    {
   	 if (player_list[i%players]==-1)
   		 continue;
   	 player_list[i%players]+=d[i];
   	 moved=true;
   	 if (player_list[i%players] > tiles-1)
   	 {
   		 player_list[i%players]=-1;
   		 cout <<(i%players)+1 <<" winner\n";
   	 }
   	 while (moved)
   	 {
   		 it=m.find(player_list[i%players]);
   		 if (it != m.end())
   			 player_list[i%players]=get<1>(it->second.data);
   		 else moved=false;
   	 }    
    }
    return;
}
 
int main()
{
    cin >>board_size;
    int temp[4];
 
    int player_size;
    cin >>player_size;
 
    std::map<int, link> list;
    link temp_l;
    std::map<int, link>::iterator it;
 
    //read in snakes
    int snake_size;
    cin >>snake_size;
    //cout <<"snake size is " <<snake_size <<'\n';
    for (int i=0; i < snake_size; ++i)
    {
   	 cin >>temp[0] >>temp[1] >> temp[2] >>temp[3];
   	 temp[0]=temp[0]*board_size+temp[1]-1;
   	 temp[2]=temp[2]*board_size+temp[3]-1;
   	 //cout <<"making node at " << temp[0] <<'\n';
   	 temp_l={std::make_tuple(temp[0], temp[2]), 1, new link};
   	 it=list.find(temp[0]);
   	 if (it !=list.end())
   		 append(it->second, &temp_l);
   	 else list[temp[0]]=temp_l;
    }
 
    
    //read in ladders
    int ladder_size;
    cin >>ladder_size;
    for (int i=0; i < ladder_size; ++i)
    {
   	 cin >>temp[0] >>temp[1] >> temp[2] >>temp[3];
   	 temp[0]=temp[0]*board_size+temp[1]-1;
   	 temp[2]=temp[2]*board_size+temp[3]-1;
   	 //cout <<"making node at " <<temp[2] <<'\n';
   	 temp_l={make_tuple(temp[2],temp[0]), 2, new link};
   	 it=list.find(temp[2]);
   	 if (it !=list.end())
   		 append(it->second, &temp_l);
   	 else list[temp[2]]=temp_l;
    }
 
 
    //dice rolls
    int num_dice;
    cin >>num_dice;
    int dice[num_dice];
    for (int i=0; i < num_dice; ++i)
    {
   	 cin >>temp[0] >>temp[1];
   	 dice[i]=temp[0]+temp[1];
    }
 
 
    process(list, dice, num_dice, player_size);
 
}
