import numpy as np
from bringingData import bring
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_percentage_error
from sklearn.cluster import KMeans, AgglomerativeClustering
import statistics
from sklearn.neural_network import MLPRegressor
from sklearn.tree import DecisionTreeRegressor
from collections import Counter
from config import names
x, y, data = bring()

#section tree class

def get_score():
    clf = DecisionTreeRegressor(random_state=241)
    x_train, x_test, y_train, y_test = train_test_split(
        x, y, test_size=0.01, random_state=42)
    clf.fit(x_train, y_train)

    tree_predict = clf.predict(x_test)
    print(names)
    print(clf.feature_importances_)
    tree_error = mean_absolute_percentage_error(np.array(y_test), tree_predict)

    mlp = MLPRegressor(max_iter=2000, n_iter_no_change=20,
                        activation='relu', alpha=0.01, hidden_layer_sizes=[100], tol=0.0000001)
    mlp.fit(x_train, y_train)
    mlp_predict = mlp.predict(x_test)
    mlp_error = mean_absolute_percentage_error(np.array(y_test), mlp_predict)

    reg = LinearRegression()
    reg.fit(x_train, y_train)
    reg_predict = reg.predict(x_test)
    reg_error = mean_absolute_percentage_error(y_true=y_test, y_pred=reg_predict)
    return {
        'mlp': mlp_error,
        'tree': tree_error,
        'reg': reg_error
    }

#section params
def get_params():
    average = sum(y)/len(y)
    min_val = min(y)
    max_val = max(y)
    median = statistics.median(y)
    return {'average': average, 'min': min_val, 'max': max_val, 'median': median}

#section predict

def calculate_class():
    kmeans = KMeans(n_clusters=3)
    kmeans_dict = {}
    agg_clust = AgglomerativeClustering(n_clusters=3)
    agg_clust_dict = {}

    corr = data[['math score', 'reading score', 'writing score']]
    kmeans.fit(corr.values)
    all_predict_kmeans = kmeans.predict(corr.values)
    # print(Counter(all_predict_kmeans))
    for i in range(len(all_predict_kmeans)):
        kmeans_dict[str(all_predict_kmeans[i])] = data.values[i][8]
        if len(kmeans_dict) == 3:
            break
    min_val = kmeans_dict['0']
    max_val = kmeans_dict['0']
    for key, val in kmeans_dict.items():
        if val > max_val:
            max_val = val
        if val < min_val:
            min_val = val
    for key, val in kmeans_dict.items():
        if val == max_val:
            kmeans_dict[key] = "Лучший класс"
        elif val == min_val:
            kmeans_dict[key] = "Худший класс"
        else:
            kmeans_dict[key] = "Средний класс"
    # print(kmeans_dict)


    agg_clust.fit(corr.values)
    all_predict_agg = agg_clust.fit_predict(corr.values)
    for i in range(len(all_predict_agg)):
        agg_clust_dict[str(all_predict_agg[i])] = data.values[i][8]
        if len(agg_clust_dict) == 3:
            break
    # print(Counter(agg_clust_dict))
    min_val = agg_clust_dict['0']
    max_val = agg_clust_dict['0']
    for key, val in agg_clust_dict.items():
        if val > max_val:
            max_val = val
        if val < min_val:
            min_val = val
    for key, val in agg_clust_dict.items():
        if val == max_val:
            agg_clust_dict[key] = "Лучший класс"
        elif val == min_val:
            agg_clust_dict[key] = "Худший класс"
        else:
            agg_clust_dict[key] = "Средний класс"
    # print(agg_clust_dict)
    counter_means = Counter(all_predict_kmeans)
    counter_agg = Counter(all_predict_agg)
    res = {
        'kmeans': {
            'dict': kmeans_dict,
            'stat': {
                '0': counter_means[0],
                '1': counter_means[1],
                '2': counter_means[2]
            }
        },
        'agg': {
            'dict': agg_clust_dict,
            'stat': {
                '0': counter_agg[0],
                '1': counter_agg[1],
                '2': counter_agg[2]
            }
        }
    }
    return res

