#include <Arduino.h>

#if USE_ADAFRUIT_GFX
#include "Adafruit_GFX/glcdfont.c"
#include "Adafruit_GFX/Adafruit_GFX.cpp"
#include "Adafruit_GFX/fontconvert/fontconvert.c"
#endif

#if USE_ADAFRUIT_PCD8544
#include "Adafruit_PCD8544/Adafruit_PCD8544.cpp"
#endif

#if USE_BUTTONS
#include "Buttons/buttons.cpp"
#endif

#if USE_EEPROM
//#include "EEPROM/EEPROM.cpp"
#endif

#if USE_ESPLORA
#include "Esplora/Esplora.cpp"
#endif

#if USE_ETHERNET
#include "Ethernet/EthernetClient.cpp"
#include "Ethernet/EthernetServer.cpp"
#include "Ethernet/Dns.cpp"
#include "Ethernet/EthernetUdp.cpp"
#include "Ethernet/Ethernet.cpp"
#include "Ethernet/Dhcp.cpp"
#include "Ethernet/utility/socket.cpp"
#include "Ethernet/utility/w5100.cpp"
#endif

#if USE_FIRMATA
#include "Firmata/Firmata.cpp"
#endif

#if USE_GSM
#include "GSM/GSM3ShieldV1DataNetworkProvider.cpp"
#include "GSM/GSM3MobileAccessProvider.cpp"
#include "GSM/GSM3ShieldV1MultiServerProvider.cpp"
#include "GSM/GSM3MobileCellManagement.cpp"
#include "GSM/GSM3ShieldV1ModemCore.cpp"
#include "GSM/GSM3MobileClientProvider.cpp"
#include "GSM/GSM3ShieldV1SMSProvider.cpp"
#include "GSM/GSM3MobileNetworkProvider.cpp"
#include "GSM/GSM3ShieldV1.cpp"
#include "GSM/GSM3ShieldV1ScanNetworks.cpp"
#include "GSM/GSM3ShieldV1VoiceProvider.cpp"
#include "GSM/GSM3ShieldV1BaseProvider.cpp"
#include "GSM/GSM3ShieldV1ModemVerification.cpp"
#include "GSM/GSM3ShieldV1ClientProvider.cpp"
#include "GSM/GSM3SMSService.cpp"
#include "GSM/GSM3ShieldV1AccessProvider.cpp"
#include "GSM/GSM3MobileSMSProvider.cpp"
#include "GSM/GSM3ShieldV1MultiClientProvider.cpp"
#include "GSM/GSM3MobileMockupProvider.cpp"
#include "GSM/GSM3ShieldV1BandManagement.cpp"
#include "GSM/GSM3ShieldV1PinManagement.cpp"
#include "GSM/GSM3MobileNetworkRegistry.cpp"
#include "GSM/GSM3ShieldV1ServerProvider.cpp"
#include "GSM/GSM3CircularBuffer.cpp"
#include "GSM/GSM3MobileServerService.cpp"
#include "GSM/GSM3MobileServerProvider.cpp"
#include "GSM/GSM3ShieldV1CellManagement.cpp"
#include "GSM/GSM3SoftSerial.cpp"
#include "GSM/GSM3MobileDataNetworkProvider.cpp"
#include "GSM/GSM3ShieldV1DirectModemProvider.cpp"
#include "GSM/GSM3MobileVoiceProvider.cpp"
#include "GSM/GSM3MobileClientService.cpp"
#include "GSM/GSM3VoiceCallService.cpp"
#endif

#if USE_LIQUIDCRYSTAL
#include "LiquidCrystal/src/LiquidCrystal.cpp"
#endif

#if USE_ROBOTIRREMOTE
#include "RobotIRremote/IRremoteTools.cpp"
#include "RobotIRremote/IRremote.cpp"
#endif

#if USE_ROBOT_CONTROL
#include "Robot_Control/Squawk.cpp"
#include "Robot_Control/Sensors.cpp"
#include "Robot_Control/communication.cpp"
#include "Robot_Control/ArduinoRobot.cpp"
#include "Robot_Control/Motors.cpp"
#include "Robot_Control/glcdfont.c"
#include "Robot_Control/Arduino_LCD.cpp"
#include "Robot_Control/RobotSdCard.cpp"
#include "Robot_Control/SquawkSD.cpp"
#include "Robot_Control/keyboard.cpp"
#include "Robot_Control/lcd.cpp"
#include "Robot_Control/SdCard.cpp"
#include "Robot_Control/information.cpp"
#include "Robot_Control/Multiplexer.cpp"
#include "Robot_Control/Melody.cpp"
#include "Robot_Control/Fat16.cpp"
#include "Robot_Control/EEPROM_I2C.cpp"
#include "Robot_Control/helper.cpp"
#include "Robot_Control/Compass.cpp"
#include "Robot_Control/EasyTransfer2.cpp"
#include "Robot_Control/utility/Adafruit_GFX.cpp"
#include "Robot_Control/utility/RobotTextManager.cpp"
#include "Robot_Control/utility/VirtualKeyboard.cpp"
#endif

#if USE_ROBOT_MOTOR
#include "Robot_Motor/EasyTransfer2.cpp"
#include "Robot_Motor/ArduinoRobotMotorBoard.cpp"
#include "Robot_Motor/Multiplexer.cpp"
#include "Robot_Motor/lineFollow.cpp"
#endif

#if USE_SD
#include "SD/File.cpp"
#include "SD/SD.cpp"
#include "SD/utility/SdVolume.cpp"
#include "SD/utility/SdFile.cpp"
#include "SD/utility/Sd2Card.cpp"
#endif

#if USE_SPI
#include "SPI/SPI.cpp"
#endif

#if USE_SERVO
#include "Servo/Servo.cpp"
#endif

#if USE_SOFTWARESERIAL
#include "SoftwareSerial/SoftwareSerial.cpp"
#endif

#if USE_STEPPER
#include "Stepper/Stepper.cpp"
#endif

#if USE_TFT
#include "TFT/TFT.cpp"
#include "TFT/utility/Adafruit_ST7735.cpp"
#include "TFT/utility/glcdfont.c"
#include "TFT/utility/Adafruit_GFX.cpp"
#endif

#if USE_TIMERONE_MASTER
#include "TimerOne-master/TimerOne.cpp"
#endif

#if USE_WIFI
#include "WiFi/WiFi.cpp"
#include "WiFi/WiFiClient.cpp"
#include "WiFi/WiFiUdp.cpp"
#include "WiFi/WiFiServer.cpp"
#include "WiFi/utility/spi_drv.cpp"
#include "WiFi/utility/server_drv.cpp"
#include "WiFi/utility/wifi_drv.cpp"
#include "WiFi/utility/socket.c"
#endif

#if USE_WIRE
#include "Wire/Wire.cpp"
#include "Wire/utility/twi.c"
#endif
