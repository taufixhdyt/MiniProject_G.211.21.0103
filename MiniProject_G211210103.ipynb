#melakukan import panda & matplotlib
import pandas as pd
import matplotlib.pyplot as plt
#mengambil dataset
dataset = pd.read_csv('https://dqlab-dataset.s3-ap-southeast-1.amazonaws.com/retail_raw_reduced.csv')
print()

#mengimport datetime
import datetime
#menampilkan order pada kolom teratas
dataset['order_month'] = dataset['order_date'].apply(lambda x: datetime.datetime.strptime(x, "%Y-%m-%d").strftime('%y-%m'))
print(dataset.head())

# kolom order_month
dataset['order_month'] = dataset['order_date'].apply(lambda x: datetime.datetime.strptime(x, "%Y-%m-%d").strftime('%Y-%m'))
# kolom gmv
dataset['gmv'] = dataset['item_price'] * dataset['quantity']
#ukuran 10x5
plt.figure(figsize=(10, 5))
#mengambil orderan pada bulan desember
dataset[dataset['order_month']=='2019-12'].groupby(['order_date'])['customer_id'].nunique().plot(color='b', marker='.', linewidth=2)
plt.title('Grafik Pembelian Bulan Desember 2019', loc='center', pad=30, fontsize=15, color='black')
plt.xlabel('Tanggal Order', fontsize=12, color='g')
plt.ylabel('Jumlah Customer', fontsize=12, color='r')
plt.grid(color='black', linestyle=':', linewidth=0.5)
plt.ylim(ymin=0)
plt.show()

#nama variabelnya top_5_brands
top_brands = (dataset[dataset['order_month']=='2019-12'].groupby('brand')['quantity']
                .sum()
                .reset_index()
                .sort_values(by='quantity',ascending=False)
                .head(5))
dataset_top_5_brands_dec = dataset[(dataset['order_month']=='2019-12') & (dataset['brand'].isin(top_brands['brand'].to_list()))]
print(top_brands)

#pengelompokan data
dataset_top_5_brands_dec.groupby(['order_date','brand'])['quantity'].sum().unstack().plot(marker='.', cmap='plasma')
plt.title('Kuantitas Harian Penjualan Desember 2019 (Breakdown)',loc='center',pad=30, fontsize=15, color='red')
#memberi keterangan
plt.xlabel('Order Date', fontsize = 12)
plt.ylabel('Quantity',fontsize = 12)
#visualisasi grafik
plt.grid(color='darkgray', linestyle=':', linewidth=0.5)
plt.ylim(ymin=0)
plt.legend(loc='upper center', bbox_to_anchor=(1.1, 1), shadow=True, ncol=1)
plt.annotate('Lonjakan', xy=(7, 300), xytext=(8, 250),
             weight='bold', color='red',
             arrowprops=dict(arrowstyle='->',
                             connectionstyle="arc3",
                             color='red'))
plt.gcf().set_size_inches(10, 5)
plt.tight_layout()
plt.show()

#membuat plot terbuka
plt.clf()
#mengambil data product
dataset_top_5_brands_dec.groupby('brand')['product_id'].nunique().sort_values(ascending=False).plot(kind='bar', color='blue')
#visualisasi (plt.show())
plt.title('Jumlah Produk yang Terjual Pada Desember 2019',loc='center',pad=30, fontsize=15, color='red')
plt.xlabel('Brand', fontsize = 12)
plt.ylabel('Number of Products',fontsize = 12)
plt.ylim(ymin=0)
plt.xticks(rotation=0)
plt.show()

dataset_top_5_brands_dec_per_product = dataset_top_5_brands_dec.groupby(['brand','product_id'])['quantity'].sum().reset_index()
#kolom menandai product yang terjual >= 100 dan <100
dataset_top_5_brands_dec_per_product['quantity_group'] = dataset_top_5_brands_dec_per_product['quantity'].apply(lambda x: '>= 100' if x>=100 else '< 100')
dataset_top_5_brands_dec_per_product.sort_values('quantity',ascending=False,inplace=True)
#mengurutkan brand berdasarkan jumlah produk
s_sort = dataset_top_5_brands_dec_per_product.groupby('brand')['product_id'].nunique().sort_values(ascending=False)
#visualisasi data
dataset_top_5_brands_dec_per_product.groupby(['brand','quantity_group'])['product_id'].nunique().reindex(index=s_sort.index, level='brand').unstack().plot(kind='bar', stacked=True)
plt.title('Penjualan Produk diatas 100 dan dibawah 100 Desember 2019',loc='center',pad=30, fontsize=15, color='red')
plt.xlabel('Brand', fontsize = 12)
plt.ylabel('Jumlah Produk',fontsize = 12)
plt.ylim(ymin=0)
plt.xticks(rotation=0)
plt.show()

plt.figure(figsize=(10,5))
#mengambil brand berdasarkan product_id dan item_price
plt.hist(dataset_top_5_brands_dec.groupby('product_id')['item_price'].median(), bins=10, stacked=True, range=(1,2000000), color='aqua')
plt.title('Harga Produk TOp 5 Brands Desember 2019',fontsize=15, color='red')
plt.xlabel('Median Harga', fontsize = 12)
plt.ylabel('Jumlah Produk',fontsize = 12)
plt.xlim(xmin=0,xmax=2000000)
plt.show()

data_per_product_top_5_brands_dec = dataset_top_5_brands_dec.groupby('product_id').agg({'quantity': 'sum', 'gmv':'sum', 'item_price':'median'}).reset_index()
#scatter plot
plt.figure(figsize=(10,8))
plt.scatter(data_per_product_top_5_brands_dec['quantity'],data_per_product_top_5_brands_dec['gmv'], marker='+', color='blue')
plt.title('Korelasi Kuantitas dan GMV Top 5 Brands Desember 2019',fontsize=15, color='red')
plt.xlabel('Quantity', fontsize = 12)
plt.ylabel('GMV (in Millions)',fontsize = 12)
plt.xlim(xmin=0,xmax=300)
plt.ylim(ymin=0,ymax=200000000)
labels, locations = plt.yticks()
plt.yticks(labels, (labels/1000000).astype(int))
plt.show()


plt.clf()
#mengambil brand berdasarkan product_id dan item_price
data_per_product_top_5_brands_dec = dataset_top_5_brands_dec.groupby('product_id').agg({'quantity': 'sum', 'gmv':'sum', 'item_price':'median'}).reset_index()
#scatter plot
plt.figure(figsize=(10,8))
plt.scatter(data_per_product_top_5_brands_dec['item_price'],data_per_product_top_5_brands_dec['quantity'], marker='o', color='green')
plt.title('Correlation of Quantity and GMV per Product\nTop 5 Brands in December 2019',fontsize=15, color='blue')
plt.xlabel('Price Median', fontsize = 12)
plt.ylabel('Quantity',fontsize = 12)
plt.xlim(xmin=0,xmax=2000000)
plt.ylim(ymin=0,ymax=250)
plt.show()
