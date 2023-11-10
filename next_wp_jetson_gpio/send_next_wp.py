import rclpy
from rclpy.node import Node
from std_srvs.srv import Trigger
import Jetson.GPIO as GPIO

input_pin = 10
# prev_value = None
# GPIO.setmode(GPIO.BCM)
# GPIO.setup(input_pin,GPIO.IN)
# value = GPIO.input(input_pin)

# if value != prev_value:
#     if value == GPIO.HIGH:
#         print("pushed switch  next_wp service_call!!")
#     if value == GPIO.LOW:
#         pass
# else:
#     pass

# prev_value = value

class Nextwpjetsongpio(Node):
    def __init__(self): 
        super().__init__('next_wp_jetson_gpio')
        self.prev_value = None
        print("start next_wp node")
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(input_pin,GPIO.IN)
        self.value = GPIO.input(input_pin)
        self.start_wp_nav_srv = self.create_client(Trigger,"next_wp")
        while not self.start_wp_nav_srv.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('service not available, waiting again...')
        self.req = Trigger.Request()
        self.create_timer(1.0, self.gpio_read)


    def gpio_read(self):
        # print("kani")
        if self.value != self.prev_value:
            if self.value == GPIO.HIGH:
                self.start_wp_nav_srv.call_async(self.req)
                print("pushed switch  next_wp service_call!!")
        if self.value == GPIO.LOW:
            pass
        else:
            pass
        self.prev_value = self.value
def main(args=None):
    try:
        rclpy.init(args=args)
        next_wp_node = Nextwpjetsongpio()
        rclpy.spin(next_wp_node)
    except KeyboardInterrupt:
        pass
    finally:
        next_wp_node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()