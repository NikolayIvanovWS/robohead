## Установка зависимостей для пакета voice_recognizer_pocketsphinx

```
cd ~/robohead_ws/src/robohead/voice_recognizer_pocketsphinx/config
```

### Скачать языковую модель

> [!NOTE]
> Иногда быстрее бывает скачать файл по ссылке на ноут и перекинуть через FileZila на голову.

```
wget https://downloads.sourceforge.net/project/cmusphinx/Acoustic%20and%20Language%20Models/Russian/zero_ru_cont_8k_v3.tar.gz

tar -xf zero_ru_cont_8k_v3.tar.gz

rm -r zero_ru_cont_8k_v3.tar.gz
```

## Конфигурация голосовых команд:

```
cd robohead_ws/src/robohead/voice_recognizer_pocketsphinx/config/ru4sphinx/text2dict/

./dict2transcript.pl /home/pi/robohead_ws/src/robohead/robohead_controller/config/voice_recognizer_pocketsphinx/dictionary.txt /home/pi/robohead_ws/src/robohead/robohead_controller/config/voice_recognizer_pocketsphinx/dictionary.dict
```

## Получение файлов озвучки для робоголовы

Сайт: [VoiceBot](https://voicebot.su/)

### Параметры 

- **Голос**:
  - Антон
- **Скорость**:
  - 0.9
- **Высота**:
  - 0.0
- **Громкость**:
  - 0 dB
- **Эмоции**:
  - Радостный
