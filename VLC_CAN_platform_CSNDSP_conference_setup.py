#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Vlc Can Platform Csndsp Conference Setup
# Author: Vicente Matus
# Generated: Sun Feb 11 22:37:17 2018
##################################################

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

from gnuradio import analog
from gnuradio import audio
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio import uhd
from gnuradio import wxgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.wxgui import forms
from gnuradio.wxgui import scopesink2
from grc_gnuradio import wxgui as grc_wxgui
from optparse import OptionParser
import time
import wx


class VLC_CAN_platform_CSNDSP_conference_setup(grc_wxgui.top_block_gui):

    def __init__(self):
        grc_wxgui.top_block_gui.__init__(self, title="Vlc Can Platform Csndsp Conference Setup")
        _icon_path = "/usr/share/icons/hicolor/32x32/apps/gnuradio-grc.png"
        self.SetIcon(wx.Icon(_icon_path, wx.BITMAP_TYPE_ANY))

        ##################################################
        # Variables
        ##################################################
        self.tx_gain = tx_gain = 0
        self.samp_rate = samp_rate = 1000000
        self.rx_gain = rx_gain = 0
        self.max_dev = max_dev = 75000
        self.center_freq = center_freq = 1250000
        self.audio_rate = audio_rate = 44100
        self.audio_interp = audio_interp = 1
        self.Delay = Delay = 10

        ##################################################
        # Blocks
        ##################################################
        _Delay_sizer = wx.BoxSizer(wx.VERTICAL)
        self._Delay_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_Delay_sizer,
        	value=self.Delay,
        	callback=self.set_Delay,
        	label='Delay(S)',
        	converter=forms.int_converter(),
        	proportion=0,
        )
        self._Delay_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_Delay_sizer,
        	value=self.Delay,
        	callback=self.set_Delay,
        	minimum=0,
        	maximum=100,
        	num_steps=100,
        	style=wx.SL_HORIZONTAL,
        	cast=int,
        	proportion=1,
        )
        self.Add(_Delay_sizer)
        self.wxgui_scopesink2_0_0 = scopesink2.scope_sink_f(
        	self.GetWin(),
        	title='Osciloscope',
        	sample_rate=samp_rate,
        	v_scale=0,
        	v_offset=0,
        	t_scale=0,
        	ac_couple=True,
        	xy_mode=False,
        	num_inputs=2,
        	trig_mode=wxgui.TRIG_MODE_STRIPCHART,
        	y_axis_label='Normalized Amplitude',
        )
        self.Add(self.wxgui_scopesink2_0_0.win)
        self.uhd_usrp_source_0 = uhd.usrp_source(
        	",".join(('addr=192.168.10.3', "")),
        	uhd.stream_args(
        		cpu_format="fc32",
        		channels=range(1),
        	),
        )
        self.uhd_usrp_source_0.set_samp_rate(samp_rate)
        self.uhd_usrp_source_0.set_center_freq(center_freq, 0)
        self.uhd_usrp_source_0.set_gain(rx_gain, 0)
        self.uhd_usrp_source_0.set_antenna('RX2', 0)
        self.uhd_usrp_sink_0 = uhd.usrp_sink(
        	",".join(('addr=192.168.10.2', "")),
        	uhd.stream_args(
        		cpu_format="fc32",
        		channels=range(1),
        	),
        )
        self.uhd_usrp_sink_0.set_samp_rate(samp_rate)
        self.uhd_usrp_sink_0.set_center_freq(center_freq, 0)
        self.uhd_usrp_sink_0.set_gain(tx_gain, 0)
        self.uhd_usrp_sink_0.set_antenna('TX/RX', 0)
        self.rational_resampler_xxx_1 = filter.rational_resampler_ccc(
                interpolation=int(samp_rate),
                decimation=int(audio_interp*audio_rate),
                taps=None,
                fractional_bw=None,
        )
        self.rational_resampler_xxx_0 = filter.rational_resampler_ccc(
                interpolation=int(audio_rate*audio_interp),
                decimation=int(samp_rate),
                taps=None,
                fractional_bw=None,
        )
        self.blocks_wavfile_sink_0_0 = blocks.wavfile_sink('/home/vmatusic/Documents/VLC/gnuradio_codes/CSNDSP/sent_CSNDSP.wav', 1, audio_rate, 16)
        self.blocks_wavfile_sink_0 = blocks.wavfile_sink('/home/vmatusic/Documents/VLC/gnuradio_codes/CSNDSP/received_CSNDSP.wav', 1, audio_rate, 16)
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_vff((0.200, ))
        self.blocks_delay_0 = blocks.delay(gr.sizeof_float*1, Delay)
        self.audio_sink_0 = audio.sink(int(audio_rate), '', False)
        self.analog_wfm_tx_0 = analog.wfm_tx(
        	audio_rate=int(audio_rate),
        	quad_rate=int(audio_rate*audio_interp),
        	tau=75e-6,
        	max_dev=max_dev,
        	fh=-1.0,
        )
        self.analog_wfm_rcv_0 = analog.wfm_rcv(
        	quad_rate=audio_interp*audio_rate,
        	audio_decimation=audio_interp,
        )
        self.analog_sig_source_x_0 = analog.sig_source_f(audio_rate, analog.GR_SIN_WAVE, 1000, 1, 0)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_multiply_const_vxx_0, 0))    
        self.connect((self.analog_wfm_rcv_0, 0), (self.audio_sink_0, 0))    
        self.connect((self.analog_wfm_rcv_0, 0), (self.blocks_delay_0, 0))    
        self.connect((self.analog_wfm_rcv_0, 0), (self.blocks_wavfile_sink_0, 0))    
        self.connect((self.analog_wfm_tx_0, 0), (self.rational_resampler_xxx_1, 0))    
        self.connect((self.blocks_delay_0, 0), (self.wxgui_scopesink2_0_0, 1))    
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.analog_wfm_tx_0, 0))    
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.blocks_wavfile_sink_0_0, 0))    
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.wxgui_scopesink2_0_0, 0))    
        self.connect((self.rational_resampler_xxx_0, 0), (self.analog_wfm_rcv_0, 0))    
        self.connect((self.rational_resampler_xxx_1, 0), (self.uhd_usrp_sink_0, 0))    
        self.connect((self.uhd_usrp_source_0, 0), (self.rational_resampler_xxx_0, 0))    

    def get_tx_gain(self):
        return self.tx_gain

    def set_tx_gain(self, tx_gain):
        self.tx_gain = tx_gain
        self.uhd_usrp_sink_0.set_gain(self.tx_gain, 0)
        	

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.wxgui_scopesink2_0_0.set_sample_rate(self.samp_rate)
        self.uhd_usrp_source_0.set_samp_rate(self.samp_rate)
        self.uhd_usrp_sink_0.set_samp_rate(self.samp_rate)

    def get_rx_gain(self):
        return self.rx_gain

    def set_rx_gain(self, rx_gain):
        self.rx_gain = rx_gain
        self.uhd_usrp_source_0.set_gain(self.rx_gain, 0)
        	

    def get_max_dev(self):
        return self.max_dev

    def set_max_dev(self, max_dev):
        self.max_dev = max_dev

    def get_center_freq(self):
        return self.center_freq

    def set_center_freq(self, center_freq):
        self.center_freq = center_freq
        self.uhd_usrp_source_0.set_center_freq(self.center_freq, 0)
        self.uhd_usrp_sink_0.set_center_freq(self.center_freq, 0)

    def get_audio_rate(self):
        return self.audio_rate

    def set_audio_rate(self, audio_rate):
        self.audio_rate = audio_rate
        self.analog_sig_source_x_0.set_sampling_freq(self.audio_rate)

    def get_audio_interp(self):
        return self.audio_interp

    def set_audio_interp(self, audio_interp):
        self.audio_interp = audio_interp

    def get_Delay(self):
        return self.Delay

    def set_Delay(self, Delay):
        self.Delay = Delay
        self._Delay_slider.set_value(self.Delay)
        self._Delay_text_box.set_value(self.Delay)
        self.blocks_delay_0.set_dly(self.Delay)


def main(top_block_cls=VLC_CAN_platform_CSNDSP_conference_setup, options=None):

    tb = top_block_cls()
    tb.Start(True)
    tb.Wait()


if __name__ == '__main__':
    main()
