# ADS1115 Python library

Simple Python library to use the ADS1115 chip for any Riscv based platform and can also doable for other.

# ADS1115: A precision 16 bit ADC with high amazing Accuracy with differential or single ended inputs and improve analog measurements with high resolution capability.

Is accurate to 0.01%(typ) - including all error sources.
It has a real resolution of 15bits (the MSB bit is the sign bit).
it has Very low active current ~150uA (typ).
Four single ended, or two differential inputs.

The ADS1115 is a precise 16bit ADC with four multiplexed inputs - You can use each input on its own, or in pairs for differential measurements.
It has an internal calibrated reference for high accuracy.

This ADS1115 shows how to setup the libraries to drive the chip, and take readings using different Programmable Gain Amplifier (PGA) gain settings.
It also covers how the device is able to measure small negative voltage even though it only operates using a single supply.
This makes it useful as a current sink or source measuring device.

# Important things to know about the chip :

Has 16 bit resolution (It is actually ±15 bit - See here).
Can detect from 0.187mV to 7.8uV depending on the PGA Setting.
Can sample from 8 to 860 SPS.
Has an internal voltage reference.
Has an internal PGA (Programmable Gain Amplifier).
Does not have an external reference - you use the internal reference via the PGA gain control to select the desired voltage range.

Note: The unusual thing about this chip is that it uses fixed voltage ranges set by the PGA gain.
Unlike other ADCs you choose the gain to select an allowed voltage range.
This device has a stated typical accuracy of 0.01% (but it has a maximum accuracy of 0.15%).
This accuracy includes all sources of error (voltage reference, Gain error, offset and noise).

#ADS1115 Specification :

Parameter                                        Value

Voltage Supply (VDD)                             2V0 ~ 5V5

Abs.Max VDD					                            -0.3V ~ 7V0
Measurement range				                        -300mV ~ Vdd+300mV

Interface					                              I2C

I2C rate					                             100kHz, 400kHz, 3.4MHz

Resolution					                           16 bits (±15 bits)

Data rate					                            8 ~ 860 SPS

Number of multiplexed inputs			            4

Active current					                     ~150uA (200uA max)

Power down current			                    	0.5uA (2uA max)

Offset error [1]				                      ±3 LSB

Integral Non-Linearity (INL) [1]	          	1 LSB

Gain error [1],[2], @ 25°C			            0.01% (typ) 0.15% (max)

I2C Addresses (selectable)			            0x48, 0x49, 0x4a, 0x4b

Operating temperature				                -40°C ~ 125°C

#License : Mit

#Dependencies : smbus2




