from sklearn import datasets
iris = datatasets.load_iris()
list(iris.keys())
X = iris["data"][:,3:] #largura da pétala
y = (iris["target"]==2).astype(np.int) # 1 se for Iris Virginica, caso contrário , 0

#treinando com o modelo de Regressão Logístico 

from sklearn.linear_model import LogisticRegression

log_reg = LogisticRegression()
log_reg.fit(X,y)

#Vejamos as probabilidades estimadas do modelo para flores com larguras de pétalas variando de 0 a 3 cm

X_new = np.linspace(0,3,1000).reshape(-1,1)
y_proba = log_reg.predict_proba(X_new)
plt.plot(X_new, y_proba[:,1], "g-", label="Iris-Virginica")
plt.plot(X_new, y_proba[:,0], "b--", label="Not Iris-Virginica")
