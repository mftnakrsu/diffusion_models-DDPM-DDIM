# Diffusion Models

Bu repo, Diffusion probabilistic model (DDPM) ve Diffusion-Inpainting model (DDIM) kullanılarak bir end-to-end örneğini göstermektedir. Bu model, Context-Unet mimarisi kullanılarak oluşturulmuş ve PyTorch frameworkü ile implemente edilmiştir.  

<img width="820" alt="Screenshot 2024-07-07 at 18 34 02" src="https://github.com/mftnakrsu/diffusion_models-DDPM-DDIM/assets/57320216/1d85184d-6bb7-46bc-a197-cc79cfbed81d">

## Diffusion Modelleri Nedir?

Diffusion modelleri, başlangıçta rastgele bir gürültüyle başlayarak adım adım daha gerçekçi görüntüler üreten bir olasılıksal modelleme tekniğidir. Bu teknikte, her bir adımda gürültü seviyesi azaltılır ve resim, gerçek veriye doğru giderek iyileştirilir. Başlangıçta tamamen rastgele olan bir resim, bu süreç boyunca gerçek dünya verilerine daha fazla benzeyen bir hal alır. Gürültünün azaltılması ve verinin iyileştirilmesi adımları matematiksel olarak yönetilir, bu da modelin istikrarlı ve güvenilir sonuçlar üretmesini sağlar. Diffusion modelleri, özellikle yapay zeka, görüntü işleme ve sanat alanlarında kullanılarak, gerçekçi görüntü sentezi ve eksik bilgi tamamlama gibi pek çok uygulamada etkili bir şekilde kullanılır.

![U-Net Architecture Overview](https://deepsense.ai/wp-content/uploads/2023/03/Overview-of-U-Net-architecture.jpeg)

ContextUnet, diffüzyon modellerinde kullanılan bir derin öğrenme modelidir ve rastgele gürültülü bir başlangıç resmini adım adım daha gerçekçi hale getirmek için tasarlanmıştır. Model, öncelikle giriş katmanında resmi işler ve başlangıç evrişim bloğu ile temsil eder. Ardından, down-sampling yolu boyunca resmin soyutlanmış özelliklerini çıkarır ve özellik haritalarını artırarak daha düşük boyutlu bir özet oluşturur. Vectorization ve embedding, özellik haritalarını time steps ve contextual labels ile zenginleştirir, bu da modelin daha derin katmanlarda daha etkili çalışmasını sağlar. up-sampling, önceki özellikleri yeniden boyutlandırarak ve birleştirerek daha yüksek çözünürlüklü bir çıktı elde etmeyi amaçlar. Son olarak, çıkış katmanı, işlenmiş özellik haritalarını başlangıçta gürültülü olan resmin orijinal boyut ve kanal sayısına sahip gerçekçi bir çıktıya dönüştürür. Bu yapı, ContextUnet'in diffüzyon modellerinde kullanıldığında, daha doğru ve anlamlı görüntü sentezlemesini sağlar, böylece modelin performansı ve sonuçların kalitesi artar. Örneğin, başlangıçta rastgele piksellerle başlayan bir resmi adım adım işleyerek, nesnelerin ve detayların belirginleştiği gerçekçi bir görüntü elde edilebilir.

## Veriseti   

1788 adet 16x16 piksel boyutunda sprite görüntüsünü içerir. Sprite görüntüleri genellikle video oyunlarında karakterler, nesneler veya arka planlar gibi grafik öğeleri temsil etmek için kullanılan küçük ve genellikle animasyonlu grafiklerdir. 
Daha fazla bilgi için [Hugging Face Datasets](https://huggingface.co/datasets/ashis-palai/sprites_image_dataset/blob/main/sprites_1788_16x16.npy) sayfasını ziyaret edebilirsiniz.

## Kaynaklar

Sprites by ElvGames, [FrootsnVeggies](https://zrghr.itch.io/froots-and-veggies-culinary-pixels) and  [kyrise](https://kyrise.itch.io/)   
Code modified https://github.com/cloneofsimo/minDiffusion   
Diffusion model is based on [Denoising Diffusion Probabilistic Models](https://arxiv.org/abs/2006.11239) and [Denoising Diffusion Implicit Models](https://arxiv.org/abs/2010.02502)
