class IPaddress(object):
      def __init__(self,ipaddress,mask):
          self.ipaddress = ipaddress
          self.mask = mask
      def getMask(self):
          if self.mask > 32 or self.mask < 0:
             print('error:mask should in range 0~32')
          num_binary = [128,64,32,16,8,4,2,1]
          mask = []
          num,reminder = divmod(self.mask,8)
          for i in range(num):
              mask.append(255)
          sum = 0
          for i in range(reminder):
              sum = sum + num_binary[i]
          mask.append(sum)
          if len(mask) == 4:
             return mask
          else :
              for i in range(4-len(mask)):
                  mask.append(0)
          return mask

      def getNetwork(self):
          network = []
          mask = []
          mask = self.getMask()
          for i in range(4):
             temp = 0
             temp = (self.ipaddress[i] & mask[i])
             network.append(temp)
          return network
      def getAddress(self):
          return self.ipaddress
      def getWildcard_mask(self):
          n = [255,255,255,255]
          mask = []
          mask = self.getMask()
          for i in range(4):
              n[i] = n[i] - mask[i]
          return n
      def __str__(self):
          return str(self)



ipv4 = IPaddress([10,0,1,7],24)
print(ipv4.getMask())
print(ipv4.getNetwork())
print(ipv4.getWildcard_mask())
