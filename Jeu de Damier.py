from tkinter import*
class avance():
    def __init__(self,i=0):
        global N1
        self.i,self.x,self.y,self.x1,self.y1,self.i1,self.i2=i,0,0,0,0,0,N1*2
        self.C,self.j,self.j1=[0]*4,-1,-1
        
    def Taçage_Du_Tableau(self):
        for i in range(0,wid+wid//N1-3,Co):
            can.create_line(i+3,Co*2,i+3,hei-Co*2-3,fill="black",width=2) #vertical
            can.create_line(3,i+Co*2,wid,i+Co*2,fill="black",width=2) #horizontal
        for j in range(0,wid-3,Co*2):
            for i in range(0,wid-3,Co*2):
                can.create_line(i+Co//2+2.5,j+Co*2,i+27.5,j+Co*3,fill="maroon",width=48)
                can.create_line(i+Co*3//2+2.5,j+Co*3,i+Co*3//2+2.5,j+Co*4,fill="maroon",width=48)
        Class.Traçage_Des_Pions()

    def Traçage_Des_Pions(self):
        for j in range(0,Co*3+1,Co):
            for i in range(0,Co*8+1,Co*2):
                if(j%(Co*2)==0):
                    Pion_B.append(can.create_oval(Co//2+3-r+i,Co*5//2-r+j,Co//2+3+r+i,Co*5//2+r+j,fill=Coul_B))
                    B.append([Co//2+3-r+i,Co*5//2-r+j,Co//2+3+r+i,Co*5//2+r+j])
                    Pion_N.append(can.create_oval(Co//2+3-r+i,Co*17//2-r+j,Co//2+3+r+i,Co*17//2+r+j,fill=Coul_N))
                    N.append([Co//2+3-r+i,Co*17//2-r+j,Co//2+3+r+i,Co*17//2+r+j])
                if(j%(Co*2)!=0):
                    Pion_B.append(can.create_oval(Co*3//2+3-r+i,Co*5//2-r+j,Co*3//2+3+r+i,Co*5//2+r+j,fill=Coul_B))
                    B.append([Co*3//2+3-r+i,Co*5//2-r+j,Co*3//2+3+r+i,Co*5//2+r+j])
                    Pion_N.append(can.create_oval(Co*3//2+3-r+i,Co*17//2-r+j,Co*3//2+3+r+i,Co*17//2+r+j,fill=Coul_N))
                    N.append([Co*3//2+3-r+i,Co*17//2-r+j,Co*3//2+3+r+i,Co*17//2+r+j])    

    def Recommencer(self):
        can.delete(ALL)
        Class.Taçage_Du_Tableau()
        #Class.__init__(0)
        
    def Pointeur(self,event):
        global B,N,N1,wid,hei,Co,b,Pion_B1,Pion_N1
        if(self.i==0):self.x,self.y=event.x,event.y
        elif(self.i==1 or self.i==2):self.x1,self.y1=event.x,event.y
        Cax,Cay,A,A1,A2,C,k=[0]*N1*9,[0]*N1*9,[0]*4,[0]*4,[0]*4,[0]*4,0
        #print(self.i,B,N)
        for j in range(0,Co*2,Co):
            for i in range(0,wid-Co//2+3,Co):
                Cax[k],Cay[k]=Co//2+3+i,Co//2+j
                k+=1
        for i in range(0,hei-Co*5,Co*2):
            for j in range(0,wid-Co//2+3,Co*2):
                Cax[k],Cay[k]=Co//2+3+j,Co*5//2+i
                k+=1
            for j in range(0,wid-Co//2+3,Co*2):
                Cax[k],Cay[k]=Co*3//2+3+j,Co*7//2+i
                k+=1
        for j in range(0,Co*2,Co):
            for i in range(0,wid-Co//2+3,Co):
                Cax[k],Cay[k]=Co//2+3+i,Co*25//2+j
                k+=1
        j,j1,a,a1,a2,a3,N1=-1,-1,0,[0]*4,0,[0]*4,N1*2
        D,D1,Coul_B,Coul_N=[78,178,278,378,478,575],[28,128,228,328,428,125],"dark green","yellow"
        for i in range(N1-1,-1,-1):
            if(B[i][0]<=self.x and self.x<=B[i][2] and B[i][1]<=self.y and self.y<=B[i][3]):
                j,self.i=i,1
                break
        for i in range(N1):
            if(N[i][0]<=self.x and self.x<=N[i][2] and N[i][1]<=self.y and self.y<=N[i][3]):
                j1,self.i=i,2
                break
        u,u1,u2,u3,b,b1=0,0,0,0,0,[0]*4
        for i in range(k):
            if(Cax[i]-r<=self.x and self.x<=Cax[i]+r and Cay[i]-r<=self.y and self.y<=Cay[i]+r):
                C=[Cax[i]-r,Cay[i]-r,Cax[i]+r,Cay[i]+r]
                break
        for i in range(k):
            if(Cax[i]-r<=self.x1 and self.x1<=Cax[i]+r and Cay[i]-r<=self.y1 and self.y1<=Cay[i]+r):
                print("self.i=",self.i,"self.C=",self.C)
                if(self.i==1 and abs(self.C[0]+r-Cax[i])==Co*2 or abs(self.C[1]+r-Cay[i])==Co*2):
                    for k2 in range(N1):
                        if((Cax[i]+self.C[0]+r)//2==B[k2][0]+r and (Cay[i]+self.C[1]+r)//2==B[k2][1]+r):
                            C,j,self.C=self.C,self.j,[0]*4
                            break
                elif(self.i==2 and abs(self.C[0]+r-Cax[i])==Co*2 or abs(self.C[1]+r-Cay[i])==Co*2):
                    for k2 in range(N1):
                        if((Cax[i]+self.C[0]+r)//2==N[k2][0]+r and (Cay[i]+self.C[1]+r)//2==N[k2][1]+r):
                            C,j1,self.C=self.C,self.j1,[0]*4
                            break

                if(0<=j and j<N1):
                    if((C[0]+r-Cax[i]==Co or C[0]+r-Cax[i]==-Co) and C[1]+r-Cay[i]==-Co):
                        A=[Cax[i]-r,Cay[i]-r,Cax[i]+r,Cay[i]+r]
                    elif(abs(C[0]+r-Cax[i])==Co*2 or abs(C[1]+r-Cay[i])==Co*2):
                        for k2 in range(N1):
                            if((Cax[i]+C[0]+r)//2==N[k2][0]+r and (Cay[i]+C[1]+r)//2==N[k2][1]+r):
                                A,u=[Cax[i]-r,Cay[i]-r,Cax[i]+r,Cay[i]+r],1
                                A1=[Cax[self.i1]-r,Cay[self.i1]-r,Cax[self.i1]+r,Cay[self.i1]+r]
                                break
                    k1=0
                    for k in range(N1):
                        if(A!=B[k] and A!=N[k]):k1+=1
                    if(k+1==k1 and A[0]!=C[0]and A[1]!=C[1]and A[2]!=C[2]and A[3]!=C[3]and A!=[0]*4):
                        B[j],a,a1,u1=A,Pion_B[j],A,1
                        if(A1!=[0]*4):
                            N[k2],a2,a3,Pion_N1[k2]=A1,Pion_N[k2],A1,0
                            
                elif(0<=j1 and j1<N1):
                    if((C[0]+r-Cax[i]==Co or C[0]+r-Cax[i]==-Co) and C[1]+r-Cay[i]==Co):
                        A=[Cax[i]-r,Cay[i]-r,Cax[i]+r,Cay[i]+r]
                    elif(abs(C[0]+r-Cax[i])==Co*2 or abs(C[1]+r-Cay[i])==Co*2):
                        for k2 in range(N1-1,-1,-1):
                            if((Cax[i]+C[0]+r)//2==B[k2][0]+r and (Cay[i]+C[1]+r)//2==B[k2][1]+r):
                                A,u2=[Cax[i]-r,Cay[i]-r,Cax[i]+r,Cay[i]+r],1
                                A1=[Cax[k-self.i2]-r,Cay[k-self.i2]-r,Cax[k-self.i2]+r,Cay[k-self.i2]+r]
                                break
                    k1=0
                    for k in range(N1):
                        if(A!=N[k] and A!=B[k]):k1+=1
                    if(k+1==k1 and A[0]!=C[0] and A[1]!=C[1] and A[2]!=C[2] and A[3]!=C[3] and A!=[0]*4):
                        N[j1],a,a1,u3,N2=A,Pion_N[j1],A,1,A
                        if(A1!=[0]*4):
                            B[k2],a2,a3,Pion_B1[k2]=A1,Pion_B[k2],A1,0
                break
        
        if(u==1 and u1==1):self.i1+=1
        if(u2==1 and u3==1):self.i2-=1
        if(a!=0 and a1!=[0]*4):
            can.coords(a,a1)
            if(self.C==[0]*4):self.i=0
        if(b!=0 and b1!=[0]*4):
            can.coords(b,b1)
            b1=[0]*4
        if(a2!=0 and a3!=[0]*4):can.coords(a2,a3)
        a,a1,a2,a3,N1=0,[0]*4,0,[0]*4,N1//2
        self.C,self.j,self.j1=a1,j,j1

N1,Co=10,50  # N1 est Nombre de carrés par lignes et Co est coté de chaque carré
wid,hei,r=N1*Co+3,Co*(N1+4)+3,20 # wid, hei: longueur et largeur du Canevas, r: rayonde chaque cercle
Pion_B,Pion_B1,Pion_N,Pion_N1,k1=[],[0]*N1*2,[],[0]*N1*2,N1//2
B,N=[],[]
Coul_B="black"
Coul_N="white"
fen=Tk()
fen.title("Jeu de Damier")
fen.geometry(str(wid+197)+"x"+str(hei+97))
tex=Label(fen,text="Bonjour à vous et bienvenue dans mon jeux",fg="green")
tex.grid(row=1,column=1,pady=10)
can=Canvas(fen,width=wid,height=hei,bg="dark grey")
can.grid(row=2,column=1,padx=40,pady=5)
Class=avance()
Class.Taçage_Du_Tableau()
can.bind("<Button-1>",Class.Pointeur)
can.grid()
#Button(text="Recommencer",fg="red",command=Class.Recommencer).grid(row=2,column=2)
fen.mainloop()
