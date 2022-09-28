import pandas as pd
import numpy as np
import random
import functools
import time
import PySimpleGUI as ps

import kmeans as m
import hirar as hirar

import csv


def main():

    file_list_column = [
        [ps.Text("Let’s Clustering!", justification='center',
                 size=(30, 2), font=("Arial", 25))],
        [ps.Text("Browse CSV File   : "),
         ps.In(size=(25, 1), enable_events=True, key="-FILE-"),
         ps.FileBrowse(),
         ],
        [ps.Text("Amount of K          : "), ps.InputText(
            size=(25, 1), enable_events=True, key="-K-"), ],
        [ps.Text("Clustering Method  :"), ps.Checkbox('K-Means', default=True, key="-KMEANS-"),
         ps.Checkbox('Hierarchical', default=True, key="-HIRAR-")],
        [ps.Text('', justification='center', size=(60, 12), key='-RESULT-')],
        [
            ps.Text(''),
            ps.Button('Clustering'), ps.Button('Exit')
        ]
    ]

    window = ps.Window("Clustering", file_list_column)
    # myList = []

    result = []
    column = []
    row = []
    s = set()
    myList = []
    huda = []

    while True:
        event, values = window.read()
        print(values)
        filename = "data/hasil_hierar2.csv"
        table_example(filename)
        if event == 'Exit' or event == ps.WIN_CLOSED:
            break
        elif event == 'Clustering':
            if(values["-FILE-"] == ''):
                window['-RESULT-'].update('\nPlease_select_a_file')
            elif(values["-K-"] == ''):
                window["-K-"].update('\nPlease_input_amount_of_K')
            else:
                try:
                    # print(str(values['-FILE-']))
                    dfNormal = pd.read_csv(
                        values['-FILE-'])

                    dfNormal = pd.DataFrame(dfNormal)

                    val = dfNormal.values[:, 1:]
                    # print('adudu 0.3')
                    data_labels = dfNormal.values[:, :1].flatten()

                    k = 0
                    if values["-K-"] == 0:
                        values["-K-"] = m.k
                        print('nilai k = ', values["-K-"])
                        # print('adudu 0')

                    # print('adudu 0.5')

                    if (int(values["-KMEANS-"])) and (int(values["-HIRAR-"])) == True:
                        window['-RESULT-'].update(
                            '\n Please fill 1 method only')

                    elif not ((int(values["-KMEANS-"])) or (int(values["-HIRAR-"]))):
                        window['-RESULT-'].update(
                            '\n Please fill the methode method')

                    elif (int(values["-KMEANS-"])) == True:
                        euclidean_kmean = m.KMeans.euclidean(
                            val, int(values["-K-"]))
                        # kmeans = KMeans.euclidean(val, int(values["-K-"]))
                        # kmeans.run()
                        euclidean_kmean.run()

                        header_list = [
                            f'Column {i}' for i in euclidean_kmean.result]
                        # print(header_list)

                        hasil = open('data/hasil_Kmeans1.csv', 'w',
                                     newline='', encoding='utf-8')
                        # writer = csv.writer(f)
                        writer_hasil = csv.writer(hasil)
                        # writer_hasil.writerow(header_list)
                        print(euclidean_kmean.result)
                        # result.pop()
                        # result_all = header_list
                        for cluster in euclidean_kmean.result:
                            print('Kluster ', cluster, '\n')

                            # result.clear()
                            result.append("cluster " + str(cluster))
                            # result[cluster].append("cluster " + str(cluster))

                            for item in euclidean_kmean.result[cluster]:
                                result.append(
                                    data_labels[item])
                                # print(data_labels[item])
                            writer_hasil.writerow(result)
                            # row.append(result)
                        # my_df = pd.DataFrame(result)
                        # my_df.to_csv(
                            # 'data/hasil_Kmeans2.csv', index=False, header=False)
                        # print(my_df)
                            result.clear()

                        hasil.close()

                        # print(column)
                        # finalResult = set(result)
                        # writer_hasil.writerow(result)

                        # df = pd.DataFrame(row, columns=euclidean_kmean.result)
                        # df.to_csv('data/hasil_Kmeans2.csv', index=False)
                        # time.sleep(3)

                        infile = 'data/hasil_Kmeans1.csv'
                        outfile = 'data/hasil_Kmeans2.csv'

                        with open(infile, 'r', newline='', encoding='utf-8') as f:
                            reader = csv.reader(f)
                            cols = []
                            for row in reader:
                                cols.append(row)

                        with open(outfile, 'w', newline='', encoding='utf-8') as f:
                            writer = csv.writer(f)
                            for i in range(len(max(cols, key=len))):
                                writer.writerow(
                                    [(c[i] if i < len(c) else '') for c in cols])

                        filename = "data/hasil_Kmeans2.csv"
                        table_example(filename)

                        window['-RESULT-'].update(
                            '\nSuccessfully clustering_for_KMeans')

                    elif (int(values["-HIRAR-"])):
                        data = pd.read_csv(
                            values['-FILE-'])

                        label = data.values[:, [0]].flatten()
                        val = data.values[:, 1:]
                        start_time = time.time()
                        pca = hirar.PCA(n_components=3)
                        val = pca.fit_transform(val)
                        val = pd.DataFrame(val)
                        val.columns = ['P1', 'P2', 'P3']

                        val_sum = np.sum(val, axis=0)/len(val)
                        clusts = hirar.Clusters(data)
                        clusts.run()
                        print(f'Took {time.time()-start_time}s')
                        clusters = hirar.Hierarchical.castObject(
                            clusts.clusters[0])

                        hasil = open('data/hasil_hierar1.csv', 'w',
                                     newline='', encoding='utf-8')
                        # writer = csv.writer(f)
                        writer_hasil = csv.writer(hasil)

                        n_cluster = int(values["-K-"])
                        j = 0
                        for item in hirar.Clusters.splitClusters(clusters, n_cluster):
                            result.append("cluster " + str(j))

                            if isinstance(item.label, str):
                                result.append(item.label)
                            else:
                                for x in item.label:
                                    # if len(x) > 0:
                                    # print('len ', len(x))
                                    # print('item ', x)
                                    for y in x:
                                        result.append(y)

                                # print(x)

                            writer_hasil.writerow(result)
                            j += 1
                            result.clear()

                        hasil.close()

                        infile = 'data/hasil_hierar1.csv'
                        outfile = 'data/hasil_hierar2.csv'

                        with open(infile, 'r', newline='', encoding='utf-8') as f:
                            reader = csv.reader(f)
                            cols = []
                            for row in reader:
                                cols.append(row)

                        with open(outfile, 'w', encoding='utf-8') as f:
                            writer = csv.writer(f)
                            for i in range(len(max(cols, key=len))):
                                writer.writerow(
                                    [(c[i] if i < len(c) else '') for c in cols])

                        filename = "data/hasil_hierar2.csv"
                        table_example(filename)

                        window['-RESULT-'].update(
                            '\nSuccesfully run hierarchical clustering :)')

                except AssertionError as error:
                    print(error)
                    window['-RESULT-'].update('\n.CSV_file_not_found')
    window.close()

    # ambil hasil kmean dari [data_labels[item] for item in euclidean_kmean.result[cluster]]


def table_example(filename):

    if filename is not None:
        try:
            # Header=None means you directly pass the columns names to the dataframe
            df = pd.read_csv(filename, sep=',', engine='python',
                             header=None, encoding='utf-8')
            # read everything else into a list of rows                 # Press if you named your columns in the csv
            data = df.values.tolist()
            # Uses the first row (which should be column names) as columns names
            header_list = df.iloc[0].tolist()
            # Drops the first row in the table (otherwise the header names and the first row will be the same)
            data = df[1:].values.tolist()
            # print(data)
        except Exception as e:
            print(e)
            ps.popup_error('Error reading file')
            return

    layout = [
        [ps.Table(values=data,
                  headings=header_list,
                  display_row_numbers=False,
                  auto_size_columns=True, size=(1000, 500),
                  hide_vertical_scroll=False, vertical_scroll_only=False
                  #   scrollable=True
                  )]
    ]

    window = ps.Window('Table', layout, size=(1000, 500))
    # window.attributes('-fullscreen', True)
    event, values = window.read()
    window.close()


if __name__ == '__main__':
    main()
