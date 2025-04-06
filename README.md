Установка зависимостей для пакета voice_recognizer_pocketsphinx

```
cd ~/robohead_ws/src/robohead/voice_recognizer_pocketsphinx/config

# Скачать языковую модель.
# Иногда быстрее бывает скачать файл по ссылке на ноут и перекинуть через FileZilla на голову
wget https://downloads.sourceforge.net/project/cmusphinx/Acoustic%20and%20Language%20Models/Russian/zero_ru_cont_8k_v3.tar.gz

tar -xf zero_ru_cont_8k_v3.tar.gz

rm -r zero_ru_cont_8k_v3.tar.gz
```

