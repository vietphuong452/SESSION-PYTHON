maytrongkho =[
    {
        'HP': 20,

        'DELL': 50,

        'MACBOOK': 12,

        'ASUS': 30
    }
]

a={
    'TOSHIBA':10
}
b={
    'FUJITTU':15
}
c={
    'ALIENWARE': 5
}
maytrongkho.append(a)
maytrongkho.append(b)
maytrongkho.append(c)
maytrongkho[0]["DELL"] = maytrongkho[0]['DELL']+10
maytrongkho[0]["MACBOOK"] = maytrongkho[0]['MACBOOK']-2
for i in range(len(maytrongkho)):
    for j in maytrongkho[i]:
        print(j,maytrongkho[i][j],sep=":")
