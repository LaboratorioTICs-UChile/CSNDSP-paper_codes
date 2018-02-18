#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Arduino
# Generated: Fri Apr  8 00:42:43 2016
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
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import wxgui
from gnuradio.eng_option import eng_option
from gnuradio.fft import window
from gnuradio.filter import firdes
from gnuradio.wxgui import fftsink2
from gnuradio.wxgui import forms
from grc_gnuradio import wxgui as grc_wxgui
from optparse import OptionParser
import baz
import os
import wx
import wow
import serial
import syslog
import time
import sys

port = '/dev/tty.usbmodem1403621' 
ard = serial.Serial(port,9600,timeout=5)

def turnon():
    ard.write(str("2\n"))

def turnoff():
    ard.write(str("1\n"))


class arduino(grc_wxgui.top_block_gui):

    def __init__(self):
        grc_wxgui.top_block_gui.__init__(self, title="Arduino")

        ##################################################
        # Variables
        ##################################################
        self.variable_check_box_0 = variable_check_box_0 = True
        self.variable_any_code_0 = variable_any_code_0 = None
        self.variable_0 = variable_0 = 0
        self.samp_rate = samp_rate = 32000

        ##################################################
        # Blocks
        ##################################################
        self._variable_check_box_0_check_box = forms.check_box(
        	parent=self.GetWin(),
        	value=self.variable_check_box_0,
        	callback=self.set_variable_check_box_0,
        	label='variable_check_box_0',
        	true=True,
        	false=False,
        )
        self.Add(self._variable_check_box_0_check_box)
        self.wxgui_fftsink2_0 = fftsink2.fft_sink_c(
        	self.GetWin(),
        	baseband_freq=0,
        	y_per_div=10,
        	y_divs=10,
        	ref_level=0,
        	ref_scale=2.0,
        	sample_rate=samp_rate,
        	fft_size=1024,
        	fft_rate=15,
        	average=False,
        	avg_alpha=None,
        	title="FFT Plot",
        	peak_hold=False,	fft_in=False,
        	always_run=False,
        	fft_out=False,
        )
        self.Add(self.wxgui_fftsink2_0.win)
        if not hasattr(self, '_post_any_code_evaluators'):
        	self._post_any_code_evaluators = []
        	self.wxEVT_AnyCode = wxEVT_AnyCode = wx.NewEventType()
        	def _run_evaluators(event):
        		_post_any_code_evaluators = self._post_any_code_evaluators
        		if len(_post_any_code_evaluators) > 0:
        			for id, evaluator in _post_any_code_evaluators:
        				try:
        					evaluator()
        				except Exception, e:
        					print "Exception while running Any Code evaluator for '%s':" % (id), e
        			del  _post_any_code_evaluators[0:len(_post_any_code_evaluators)]
        	self._run_evaluators = _run_evaluators
        	try:
        		self.GetWin().Connect(-1, -1, wxEVT_AnyCode, _run_evaluators)
        	except:
        		pass	# FIXME
        	def _run_evaluators_later(evaluator=None):
        		if evaluator is not None:
        			self._post_any_code_evaluators += [evaluator]
        		try:
        			de = wx.PyEvent()
        			de.SetEventType(wxEVT_AnyCode)
        			wx.PostEvent(self.GetWin(), de)
        		except TypeError: 
        			pass
        		except AttributeError:	# FIXME
        			print "Cannot post message"
        	self._run_evaluators_later = _run_evaluators_later
        	_run_evaluators_later()
        def __post_evalutate_variable_any_code_0():
        	self._post_any_code_evaluators += [('variable_any_code_0', lambda: self._evalutate_variable_any_code_0(**{'variable_check_box_0': variable_check_box_0}))]
        def __evalutate_variable_any_code_0(*args, **kwds):
            try:
                if self.variable_check_box_0 == True:
                    turnon()
                elif self.variable_check_box_0 == False:
                    turnoff()
                    
                self.set_variable_any_code_0(self.variable_any_code_0)
            except AttributeError, e:
                print "AttributeError while evaulating variable_any_code_0:", e
                __post_evalutate_variable_any_code_0()
            except Exception, e:
                print "Exception while evaluating variable_any_code_0:", e
        self._evalutate_variable_any_code_0 = __evalutate_variable_any_code_0
        self.__post_evalutate_variable_any_code_0 = __post_evalutate_variable_any_code_0
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_gr_complex*1, samp_rate,True)
        self.analog_noise_source_x_0 = analog.noise_source_c(analog.GR_GAUSSIAN, 1, 0)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_noise_source_x_0, 0), (self.blocks_throttle_0, 0))    
        self.connect((self.blocks_throttle_0, 0), (self.wxgui_fftsink2_0, 0))    

    def get_variable_check_box_0(self):
        return self.variable_check_box_0

    def set_variable_check_box_0(self, variable_check_box_0):
        self.variable_check_box_0 = variable_check_box_0
        self._evalutate_variable_any_code_0(**{'variable_check_box_0': self.variable_check_box_0})
        self._variable_check_box_0_check_box.set_value(self.variable_check_box_0)

    def get_variable_any_code_0(self):
        return self.variable_any_code_0

    def set_variable_any_code_0(self, variable_any_code_0):
        self.variable_any_code_0 = variable_any_code_0

    def get_variable_0(self):
        return self.variable_0

    def set_variable_0(self, variable_0):
        self.variable_0 = variable_0

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.blocks_throttle_0.set_sample_rate(self.samp_rate)
        self.wxgui_fftsink2_0.set_sample_rate(self.samp_rate)


def main(top_block_cls=arduino, options=None):

    tb = top_block_cls()
    tb.Start(True)
    tb.Wait()


if __name__ == '__main__':
    main()
