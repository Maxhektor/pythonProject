class anObject:
    def __init__(self):
        self.name = "The name of our object"
        self.property1 = "The first property of our object"
        self.property2 = "The second property of our object"
        self.__secretProperty = "This property is not supposed to be seen"

    def anObjectFunction(self):
        print("Hello i am an object")
        print("And my name is " + self.name + "!")

    def __getSecretProperty(self):
        return self.__secretProperty


    def proxyGetSecretProperty(self):
        secretProp = self.__secretProperty
        return secretProp


