# predict and plot using just cylinders as a feature
X = auto[:, 1:2] # fixme
y = auto[:, 0] # fixme
w, y_pred, sse = linreg(X, y)

plt.plot(X, y, 'o')
plt.plot(X, y_pred, 'r')
plt.show()
