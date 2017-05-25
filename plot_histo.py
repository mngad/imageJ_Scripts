
import os.path

import matplotlib.pyplot as plt

import pandas


direc = 'F:\PHD\HUMAN\Intact\Scan_Data\Histograms'


def get_data(file_list):

    per_histo_list = []
    histo_dict = {}
    for file in file_list:

        data = pandas.read_csv(
            direc + '\\' + file,
            header=None,
            names=['GS', 'count'])
        gs = data['GS']
        count = data['count']
        gs = gs.tolist()
        count = count.tolist()
        per_histo_list.append(gs)
        per_histo_list.append(count)
        # print(per_histo_list)
        histo_dict[file[:-4]] = per_histo_list
        per_histo_list = []

    return histo_dict


def plot(data):

    fig = plt.figure()
    fig.suptitle('Histograms', fontsize=22)
    ax = fig.add_axes([0.1, 0.1, 0.6, 0.75])
    ax.set_yscale('log')
    for a in data.keys():
        ax.plot(
            data[a][0],
            data[a][1],
            label=a[:-22],
            linewidth=2)
        # print(data[i * per_spec + a][2])
        # print('i = ' + str(i) + ', a = ' + str(a))
    ax.legend(
        bbox_to_anchor=(1.05, 1.),
        loc=2,
        borderaxespad=0.,
        fontsize=9)
    plt.xlabel('GS')
    plt.ylabel('Count')
    plt.show()
    # fname = direc + '/' + str(title) + '.' + str(file_type)
    # if os.path.isfile(fname):
    #     print("File exists already")
    # else:
    #     plt.savefig(fname, bbox_inches='tight')
    plt.close()


if __name__ == "__main__":

    os.chdir(direc)
    list_of_csvs = []
    # Scan through them separating them.
    list_of_files = sorted(os.listdir(direc))
    for file in list_of_files:
        if ".csv" in file:
            list_of_csvs.append(file)
            print(file)
    data_dict = get_data(list_of_csvs)
    plot(data_dict)
