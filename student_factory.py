from abc import ABCMeta,abstractstaticmethod

class studentInterface(metaclass=ABCMeta):
    
    @abstractstaticmethod
    def marks():
        """static interface method"""

class overAchiever(studentInterface):

    def __init__(self):
        self._physics = 100
        self._chemistry = 100
        self._math = 100

    def marks(self):
        return {"physics":self._physics,"chemistry":self._chemistry,"math":self._math}

class averageJoe(studentInterface):
    
    def __init__(self):
        self._physics = 70
        self._chemistry = 70
        self._math = 70

    def marks(self):
        return {"physics":self._physics,"chemistry":self._chemistry,"math":self._math}

class underAchiever(studentInterface):
    
    def __init__(self):
        self._physics = 40
        self._chemistry = 40
        self._math = 40

    def marks(self):
        return {"physics":self._physics,"chemistry":self._chemistry,"math":self._math}


class studentFactory:

    @staticmethod
    def get_student(student):

        try:
            if student == "overAchiever":
                return overAchiever()
            if student == "averageJoe":
                return averageJoe()
            if student == "underAchiever":
                return underAchiever()
            raise AssertionError("student not found")
        except AssertionError as _e:
            print(_e)
        return None

if __name__ == "__main__":
    STUDENT_FACTORY = studentFactory.get_student("averageJoe")
    print(STUDENT_FACTORY.marks())