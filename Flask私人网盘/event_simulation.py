# -*-coding:GBK -*-
from pymouse import PyMouse
from pykeyboard import PyKeyboard
import time


class KM:
    """
        ����������ģ����ꡢ�����¼�
    """

    def __init__(self):
        self.m = PyMouse()
        self.k = PyKeyboard()

    def open_wifi(self):
        # ��wifi����ʱ�ڷ�����ת̬�²ſ���
        self.m.move(1600, 870)
        time.sleep(1)
        self.m.click(1500, 860)
        time.sleep(1)
        self.m.click(1500, 850)
        time.sleep(1)
        self.k.tap_key(self.k.escape_key)
        return 'wifi�Ѵ�/�ر�'

    def thunder_res(self):
        # Ѹ�������̣߳�ע��Ѹ��X��Ҫ��󻯣�ͼ������½ǣ���7��
        self.m.move(1314, 863)
        time.sleep(1.6)
        self.m.click(1312, 850)
        time.sleep(1)
        self.m.click(1274, 817)
        time.sleep(3)
        self.m.click(336, 160)
        time.sleep(10)
        self.m.click(336, 160)
        time.sleep(2)
        self.m.click(1511, 25)
        time.sleep(0.5)
        screen_size = self.m.screen_size()
        self.m.move(int(screen_size[0] / 2), int(screen_size[1] / 2))
        self.m.click(int(screen_size[0] / 2), int(screen_size[1] / 2))
        return 'Ѹ������������'
