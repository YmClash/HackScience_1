import random
import numpy as np
import matplotlib.pyplot as plt
import pretty_midi


from pycomposer.gancomposable._torch.conditional_gan_composer import ConditionalGANComposer
import torch
import random


print("hallo")
numbre = [random.randint(0,10) for i in range(10)]
print(numbre)


ctx = "cuda:0" if torch.cuda.is_available() else "cpu"

if torch.cuda.is_available():
    print("cuda")
else:
    print("CPU")

gan_composer = ConditionalGANComposer(

    midi_path_list=[r"C:\Users\y_mc\PycharmProjects\HackScience_1\LAB_1\MIDI\nocturne_27_2_(c)inoue.mid"],

    batch_size=20,
    seq_len=8,
    learning_rate=10,
    time_fraction=0.5,
    ctx=ctx
)


gan_composer.learn(

    iter_n=10,
    k_step=1
)



generative_loss_arr, discriminative_loss_arr,posterior_logs_arr,feature_matching_loss_arr = gan_composer.extract_logs()

log_discri = np.array(discriminative_loss_arr)
log_gen = np.array(generative_loss_arr)

for i in gan_composer.learn():
    print(i(gan_composer.extract_logs()))


plt.figure(figsize=(8,6))

plt.plot(posterior_logs_arr, label="post")
plt.plot(discriminative_loss_arr, label="disc")
plt.title("logs de posterior")
plt.xlabel("epoch = Temps")
plt.ylabel("Loss / Perte")
plt.legend()

plt.show()


gan_composer.compose(

    file_path= r"C:\Users\y_mc\PycharmProjects\HackScience_1\Lab_1\MIDI\Output\demo3.mid",

    velocity_mean=None,

    velocity_std=None

)



print("fin de programme")
