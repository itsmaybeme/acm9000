import picamera
import picamera.array
import time

def restest():
    """Ska test hur långtid det tar att ta en bild->rgb-matris"""
    with picamera.PiCamera() as camera:
        with picamera.array.PiRGBArray(camera) as output:
            ######################################
            #SETTINGS
            #Ovissentliga är utkommenterade
            ###
            #camera.resolution = (width, height)
            #camera.framerate = 10
            #camera_num=0 
            #stereo_mode='none'
            #stereo_decimate=False
            camera.sensor_mode=0 #Automatiskt av resolution och framerate
            camera.resolution= (112, 80)
            
            #led_pin=None #GPIO pin som ska styra kamerans led
            ###
            camera.sharpness = 0
            camera.contrast = 0
            camera.brightness = 50
            camera.saturation = 0
            camera.ISO = 50
            camera.video_stabilization = False
            camera.exposure_compensation = 0
            camera.exposure_mode = 'sports'
            camera.meter_mode = 'average'
            camera.awb_mode = 'auto'
            camera.image_effect = 'none'
            camera.color_effects = None
            camera.rotation = 0
            camera.hflip = True
            camera.vflip = True
            camera.crop = (0.0, 0.0, 1.0, 1.0)
            camera.image_denoise=False
            #Specifikt för camera.capture:
            uvp = True # use_video_port #Use_video_port = True, innebär att bilder tas snabbare som att det vore en video
            ######################################
            #sensor_vektor = [0, 1, 3, 4, 5, 6, 7]
            #awb_vektor=['off','auto','sunlight','cloudy','shade','tungsten','fluorescent','incandescent','flash','horizon']
            #meter_vektor=['average','spot','backlit','matrix']
            #exposure_vektor=['off','auto','night','nightpreview','backlight','spotlight','sports','snow','beach','verylong','fixedfps','antishake','fireworks']
            #color_effect_vektor=[None, (128, 128)]
            #tfvektor=[True, False]
            start=time.time()
            #camera.capture('baestuvp.jpeg',use_video_port=uvp)
            #camera.capture('baestfalseuvp.jpeg',use_video_port=False) 
            camera.capture(output, 'rgb',use_video_port=uvp) 
            #Gör något med output här
            
            end=time.time()
            taken=(time.time()-start)
            print('Att ta bild med bästa settings:'  + str(taken) + ' s')
            print('Nuvarnade exposure speed ' + str(camera.exposure_speed) +' us')
            print('Image denoise: ' + str(camera.image_denoise))
            print('Image effect: ' + str(camera.image_effect))
restest()
