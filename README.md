Oluşturulan model input olarak pi sayısının rakamları içerisinden rastgele bir noktada başlayacak şekilde
"block_size" sayısı kadar rakam alır. Verilen dizinin en son elemanından bir sonraki rakam ise 
((block_size+1). rakam) modele target olarak verilir ve eğitimler sonucunda modelin input dizisindeki
rakalara bakarak bu diziden sonra gelebilecek rakamı tahmin etmesi beklenir.

Model tahminleri için %10'un üzerinde bir başarı sağladığında eğitildiği data içerisindeki rakamlarının 
içerisinde belirli ya da belirsiz bir örüntü, düzen mantık, tekrar, vb. olduğunun kanıtı niteliğindedir. 
Modelin tahminleri %10'a yakın bir düzeyde kaldığında, her bir tahmin için 10 seçenek olduğundan, modelin 
düzen arayışında başarısız kaldığına kanaat getirilmelidir.  

Ayrıca model pi sayısı için başarısız olduğu takdirde, model için kullanılan sistemin sorun teşkil edip 
etmediğine, içerisinde dolaylı ya da dolaysız olarak bir örüntü, düzen, mantık, tekrar, vb. içeren bir 
dataset kullanarak karar verilmelidir. Model ikinci dataset eğitiminden sonra rakam tahminleri için %10'un 
üzerinde bir başarı sağladığında; modelin pi sayısı için yeterince gelişmiş olmadığı ya da pi sayısının 
tamamen rastgele olduğu yönünde iki ihtimal ortaya çıkmaktadır. Model ikinci dataset eğitiminden sonra 
rakam tahminleri için %10'a yakın bir başarı sağladığında ise modelin yeterince gelişmiş olmadığı 
kanıtlanmış olmalıdır.

----------------------------------------------------------------------------------

# Model parameters:

input_layer = 1024
hidden_layer1 = 512
hidden_layer2 = 256
hidden_layer3 = 128
(every layer passed through relu)

optimizer = Adam
criterion = CrossEntropyLoss

# Training parameters:

iters = 1000
schedule = (optimizer, step_size=50, gamma=0.75)

# Data parameters:

digit_num = 10000000

----------------------------------------------------------------------------------

Yukarıda bahsedilen ikinci data içerisinde dolaylı ya da dolaysız olarak bir örüntü, düzen, mantık, 
tekrar, vb. içermesi maksadıyla karmaşık bir matematik fonksiyonunun çıktılarından oluşturuldu: 
(create_dataset.py)

# Kullanılan formül:

int(abs((math.sin(i) * i**3 + math.log(i + 1) + math.exp(i % 10) + i**2 + 5 * i) % 10))

Parametreleri yukarda verilen model yine parametreleri yukarıda verilen eğitim koşullarında data'dan 
birçok kez geçirildi. 

Model eğitimlerin sonucunda, rakam tahminlerinde yaklaşık %20 civarında bir başarı oranı sağladı, 
ayrıca ortalama 2 civarında bir loss değerine kadar indi. Manuel testler sonucunda bariz bir tahmin 
yeteneği saptandı. 

----------------------------------------------------------------------------------

Aynı koşullardaki model hiç bir parametresi değiştirilmeden pi sayısının ilk 100 milyon rakamı üzerinden 
eğitime sokuldu. Model 100 farklı denemeye rağmen bu eğitimlerin hiçbirinde %10'un üzerinde bariz bir 
başarı oranı gösteremedi. Modelin bu başarısızlığının kaynağı olabilecek hiçbir nöral dengesizlik, 
overfitting ya da buna benzer süreç kaynaklı bir aksaklık saptanmadı. Manuel denemelerde model her dizi 
için farklı tahminler vermeye devam etti (learning schedule tekniği ile modelin bir ya da daha fazla cevapta takılıp kalması, sürekli her dizi için aynı rakaları tahmin etmeye çalışmasının önüne geçildi).
