import matplotlib.pyplot as plt
import numpy as np

MID_WEST= ['Kansas', 'Siena', 'Houston', 'Marq.', 'Auburn','Liberty','Wisconsin','N. Texas',
        'Iowa','E. TN St.', 'Duke','Belmont','Prov.', 'AZ St.', 'Kentucky','NDak St'
       ]
def mid_west(MID_WEST):
    for i in range(16):
        plt.text(0,y_space*((31-i)+.1),MID_WEST[i],fontsize=9)
        
def senarios():
    sn11 = ['Kansas',  'Marq.', 'Auburn','Wisconsin',
        'Iowa', 'Belmont','Prov.', 'Kentucky'
       ]
    for j in range(8):
        plt.text(x_space,(15.4-j)*y_space*2+.5*y_space,sn11[j],fontsize=9,color='magenta')
    sn12 = ['Kansas',  'Wisconsin',
        'Iowa',  'Kentucky'
       ]
    for k in range(4):
        plt.text(x_space*2,(7.2-k)*y_space*4+1.5*y_space,
                  sn12[k],fontsize=9,color='magenta')
    sn13 = ['Kansas',  
          'Kentucky'
       ]
    sn14 = ['Kansas',  
          ]
          
EAST= ['Kansas', 'Siena', 'Houston', 'Marq.', 'Auburn','Liberty','Wisconsin','N. Texas',
        'Iowa','E. TN St.', 'Duke','Belmont','Prov.', 'AZ St.', 'Kentucky','NDak St',
       ]
def east(EAST):
    for i in range(16):
        plt.text(0,y_space*((15-i)+.1),EAST[i],fontsize=9)
        
def senarios():
    sn11 = ['Kansas',  'Marq.', 'Auburn','Wisconsin',
        'Iowa', 'Belmont','Prov.', 'Kentucky'
       ]
    for j in range(8):
        plt.text(x_space,(15.4-j)*y_space*2+.5*y_space,sn11[j],fontsize=9,color='magenta')
    sn12 = ['Kansas',  'Wisconsin',
        'Iowa',  'Kentucky'
       ]
    for k in range(4):
        plt.text(x_space*2,(7.2-k)*y_space*4+1.5*y_space,
                  sn12[k],fontsize=9,color='magenta')
    sn13 = ['Kansas',  
          'Kentucky'
       ]
    sn14 = ['Kansas',  
          ]
          
          
          y_len = 6.5
x_len = 9
fig = plt.figure(figsize=[x_len, y_len])

y_space = y_len/34 
x_space = x_len/11
# First four

def bracket_bars(x_len,y_len,x_space,y_space):
    fs = 10
    # First round
    plt.text(0,34*y_space,'First\nRound',fontsize=fs)
    plt.text(x_len,34*y_space,'First\nRound',fontsize=fs,horizontalalignment='right')
    for i in range(32):
        plt.hlines(i*y_space,0,x_space)
        plt.hlines(i*y_space,x_len-x_space,x_len)


    # Second round
    plt.text(x_space,34*y_space,'Second\nRound',fontsize=fs)
    plt.text(x_len-x_space,34*y_space,'Second\nRound',fontsize=fs,horizontalalignment='right')
    for j in range(16):
        plt.hlines(j*y_space*2+.5*y_space,x_space,x_space*2)
        plt.hlines(j*y_space*2+.5*y_space,x_len-2*x_space,x_len-x_space)
        plt.vlines(x_space,j*y_space*2,
                   j*y_space*2+y_space
                  )
        plt.vlines(x_len-x_space,j*y_space*2,
                   j*y_space*2+y_space
                  )


    # Sweet Sixteen
    plt.text(2*x_space,34*y_space,'Sweet\nSixteen',fontsize=fs+1)
    plt.text(x_len-2*x_space,34*y_space,'Sweet\nSixteen',fontsize=fs+1,horizontalalignment='right')
    for k in range(8):
        plt.hlines(k*y_space*4+1.5*y_space,x_space*2,x_space*3)
        plt.hlines(k*y_space*4+1.5*y_space,x_len-3*x_space,x_len-2*x_space)
        plt.vlines(2*x_space,k*y_space*4+.5*y_space,
               k*y_space*4+2.5*y_space
              )
        plt.vlines(x_len-2*x_space,k*y_space*4+.5*y_space,
               k*y_space*4+2.5*y_space
              )

    # Elite Eight
    plt.text(3*x_space,34*y_space,'Elite\nEight',fontsize=fs+2)
    plt.text(x_len-3*x_space,34*y_space,'Elite\nEight',fontsize=fs+2,horizontalalignment='right')
    for l in range(4):
        plt.hlines(l*y_space*8+3.5*y_space,x_space*3,x_space*4)
        plt.hlines(l*y_space*8+3.5*y_space,x_len-4*x_space,x_len-3*x_space)
        plt.vlines(3*x_space,l*y_space*8+1.5*y_space,
           l*y_space*8+5.5*y_space
          )
        plt.vlines(x_len-3*x_space,l*y_space*8+1.5*y_space,
                   l*y_space*8+5.5*y_space
                  )

    # Final Four
    plt.text(4*x_space,34*y_space,'Final\nFour',fontsize=fs+2)
    plt.text(x_len-4*x_space,34*y_space,'Final\nFour',fontsize=fs+2,horizontalalignment='right')
    for m in range(2):
        plt.hlines(m*y_space*16+7.5*y_space,x_space*4,x_space*5)
        plt.hlines(m*y_space*16+7.5*y_space,x_len-5*x_space,x_len-4*x_space)
        plt.vlines(4*x_space,m*y_space*16+3.5*y_space,
                   m*y_space*16+11.5*y_space
                  )
        plt.vlines(x_len-4*x_space,m*y_space*16+3.5*y_space,
               m*y_space*16+11.5*y_space
              )

    # Finals
    plt.text(x_len/2,13*y_space,'Finals',fontsize=fs+4, 
             color = 'red',horizontalalignment='center')
    plt.hlines(y_space*15,x_space*3.5,x_space*4.5,
               color = 'red')
    plt.hlines(y_space*15,x_len-x_space*3.5,x_len-x_space*4.5,
               color = 'red')
    
    #National Chamption
    plt.text(x_len/2,19*y_space,'National\nChampion',fontsize=fs+5, 
             color = 'blue',horizontalalignment='center')
    plt.hlines(y_space*17,x_space*5,x_space*6,color = 'blue')

bracket_bars(x_len,y_len,x_space,y_space)
mid_west(MID_WEST)
east(EAST)
senarios()
plt.axis('off')
plt.savefig('brackt.png',dpi=300)
