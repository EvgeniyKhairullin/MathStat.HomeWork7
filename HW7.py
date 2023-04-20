import numpy as np
import scipy.stats as stats
x1 = np.array([380, 420, 290])
y1 = np.array([140, 360, 200, 900])

stats.mannwhitneyu(x1, y1)
x1 = np.array([150, 160, 165, 145, 155])
x2 = np.array([140, 155, 150, 130, 135])
x3 = np.array([130, 130, 120, 130, 125])

stats.friedmanchisquare(x1, x2, x3)
x1 = np.array([150, 160, 165, 145, 155])
x2 = np.array([140, 155, 150, 130, 135])

stats.wilcoxon(x1, x2)
x1 = np.array([56, 60, 62, 55, 71, 67, 59, 58, 64, 67])
x2 = np.array([57, 58, 69, 48, 72, 70, 68, 71, 50, 53])
x3 = np.array([57, 67, 49, 48, 47, 55, 66, 51, 54])

stats.kruskal(x1, x2, x3)
X = np.array([2.51, 2.35, 2.74, 2.56, 2.40, 2.36, 2.65, 2.7, 2.67, 2.34])

mean = X.mean()
std = X.std(ddof=1)

t_fact = (mean - 2.5) / std * np.sqrt(len(X))
t_fact
n = 10
m = 2.5

t = stats.t.ppf(0.975, 9)
print(f"t теор = {t:.2f}")

t = (mean - m) * np.sqrt(n) / std
print(f"t рассч = {t:.3f}")