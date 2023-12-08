import numpy as np
import pandas as pd

from converter import convert_all_to_num
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_percentage_error
from sklearn.cluster import KMeans, AgglomerativeClustering
import statistics
from sklearn.neural_network import MLPRegressor
from sklearn.tree import DecisionTreeRegressor
from collections import Counter

from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()

x, y, data = convert_all_to_num()
names = ["gender", "race/ethnicity", "parental level of education", "lunch", "test preparation course"]

# y = y.rolling(window=3).mean().dropna()  # метод скользящего среднего


def get_params():
    average_stat = sum(y) / len(y)
    min_stat = min(y)
    max_stat = max(y)
    median_stat = statistics.median(y)

    values_above_median = sum(1 for value in y if value > median_stat)
    values_below_median = sum(1 for value in y if value < median_stat)

    deviation_percentage = 15

    min_threshold_low = min_stat - (min_stat * deviation_percentage / 100)
    min_threshold_high = min_stat + (min_stat * deviation_percentage / 100)

    max_threshold_low = max_stat - (max_stat * deviation_percentage / 100)
    max_threshold_high = max_stat + (max_stat * deviation_percentage / 100)

    avg_threshold_low = average_stat - (average_stat * deviation_percentage / 100)
    avg_threshold_high = average_stat + (average_stat * deviation_percentage / 100)

    # Фильтруем данные по заданным границам
    near_min = sum(1 for score in y if min_threshold_low <= score <= min_threshold_high)
    near_max = sum(1 for score in y if max_threshold_low <= score <= max_threshold_high)
    near_avg = sum(1 for score in y if avg_threshold_low <= score <= avg_threshold_high)

    print(near_min)
    print(near_max)
    print(near_avg)

    return {
        'average': '{:.2f}'.format(average_stat),
        'min': '{:.2f}'.format(min_stat),
        'max': '{:.2f}'.format(max_stat),
        'median': '{:.2f}'.format(median_stat),
        'near_avg': near_avg,
        'near_min': near_min,
        'near_max': near_max,
        'values_above_median': '{:.2f}'.format(values_above_median),
        'values_below_median': '{:.2f}'.format(values_below_median)
    }


# section predict

def calculate_class():
    kmeans = KMeans(n_clusters=3)
    kmeans_dict = {}

    # Метод K-средних
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
    # МК Значения
    for key, val in kmeans_dict.items():
        if val > max_val:
            max_val = val
        if val < min_val:
            min_val = val
    # МК Метки
    for key, val in kmeans_dict.items():
        if val == max_val:
            kmeans_dict[key] = "Отличники"
        elif val == min_val:
            kmeans_dict[key] = "Троечники"
        else:
            kmeans_dict[key] = "Хорошисты"

    # print(kmeans_dict)
    counter_means = Counter(all_predict_kmeans)

    # Агломеративная кластеризация
    agg_clust = AgglomerativeClustering(n_clusters=3)
    agg_clust_dict = {}

    agg_clust.fit(corr.values)
    all_predict_agg = agg_clust.fit_predict(corr.values)
    for i in range(len(all_predict_agg)):
        agg_clust_dict[str(all_predict_agg[i])] = data.values[i][8]
        if len(agg_clust_dict) == 3:
            break
    print(Counter(agg_clust_dict))
    min_val = agg_clust_dict['0']
    max_val = agg_clust_dict['0']
    # АК Значения
    for key, val in agg_clust_dict.items():
        if val > max_val:
            max_val = val
        if val < min_val:
            min_val = val
    # АК Метки
    for key, val in agg_clust_dict.items():
        if val == max_val:
            agg_clust_dict[key] = "Отличники"
        elif val == min_val:
            agg_clust_dict[key] = "Троечники"
        else:
            agg_clust_dict[key] = "Хорошисты"
    counter_agg = Counter(all_predict_agg)

    # Вычисление значений выше медианы и ниже медианы
    kmeans_clust_medians = np.median(
        [data.values[i][8] for i in range(len(all_predict_kmeans)) if all_predict_kmeans[i] == 0]) + np.median(
        [data.values[i][8] for i in range(len(all_predict_kmeans)) if all_predict_kmeans[i] == 1]) + np.median(
        [data.values[i][8] for i in range(len(all_predict_kmeans)) if all_predict_kmeans[i] == 2])

    kmeans_clust_above_median = sum(1 for value in range(len(all_predict_kmeans)) if value > kmeans_clust_medians)
    kmeans_clust_below_median = sum(1 for value in range(len(all_predict_kmeans)) if value < kmeans_clust_medians)

    agg_clust_medians = np.median(
        [data.values[i][8] for i in range(len(all_predict_agg)) if all_predict_agg[i] == 0]) + np.median(
        [data.values[i][8] for i in range(len(all_predict_agg)) if all_predict_agg[i] == 1]) + np.median(
        [data.values[i][8] for i in range(len(all_predict_agg)) if all_predict_agg[i] == 2])

    agg_clust_above_median = sum(1 for value in range(len(all_predict_agg)) if value > agg_clust_medians)
    agg_clust_below_median = sum(1 for value in range(len(all_predict_agg)) if value < agg_clust_medians)

    res = {
        'kmeans': {
            'dict': kmeans_dict,
            'stat': {
                '0': counter_means[0],
                '1': counter_means[1],
                '2': counter_means[2]
            },
            'kmeans_clust_medians': kmeans_clust_medians,
            'kmeans_clust_above_median': kmeans_clust_above_median,
            'kmeans_clust_below_median': kmeans_clust_below_median
        },
        'agg': {
            'dict': agg_clust_dict,
            'stat': {
                '0': counter_agg[0],
                '1': counter_agg[1],
                '2': counter_agg[2],
            },
            'agg_clust_medians': agg_clust_medians,
            'agg_clust_above_median': agg_clust_above_median,
            'agg_clust_below_median': agg_clust_below_median
        }
    }
    return res


# section tree class
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
