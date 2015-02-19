knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X, y)
predictions = knn.predict(Xt)
Accuracy = sum(predictions == yt) / predictions.shape[0]
print "KNN accuracy: %.3f" % Accuracy

svc = LinearSVC(loss = 'l2')
svc.fit(X, y)
print "SVC accuracy: %.3f" % svc.score(Xt, yt)
