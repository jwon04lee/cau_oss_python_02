"""
정사각형, 원, 정삼각형의 넓이를 구해주는 모듈
"""

import math

class Line:
    """
    외부에서 접근 불가능한 필드 __length의 기본값은 1이며,
    생성자를 통해 해당 필드의 초기값을 지정할 수 있고,
    메소드 set_length와 get_length를 통해 해당 필드에 접근한다.
    """
    __length = 1

    def __init__(self, initial_value):
        """객체를 생성하여 초기값의 타입이 정수 또는 실수이고, 0보다 클 때에만 초기값을 저장하는 함수
        Args:
            initial_value: 객체가 저장할 숫자의 초기값
        Examples:
            >>> myline = figure.Line(10) # 초기 숫자 값이 10인 객체 생성
        """
        if(type(initial_value) == int or type(initial_value) == float):
            if(not initial_value <= 0):
                self.__length = initial_value
            else:
                pass
        else:
            pass
    
    def set_length(self, new_value):
        """새로운 값의 타입이 정수 또는 실수이고, 0보다 클 때에만 저장 중인 값을 새로운 값으로 변경하는 메소드
        Args:
            new_value: 숫자의 변경값
        Examples:
            >>> myline.set_length(3) # 저장 중인 값을 3으로 변경한다.
        """
        if(type(new_value) == int or type(new_value) == float):
            if(not new_value <= 0):
                self.__length = new_value
            else:
                pass
        else:
            pass
    
    def get_length(self):
        """현재 저장 중인 값을 반환하는 메소드
        Returns:
            self.__length: 현재 저장 중인 값
        Examples:
            >>> myline.get_length()
        """
        return self.__length

def area_square(s):
    """정사각형의 넓이를 구하는 함수
    Args:
        s: 정사각형의 한 변의 길이
    Returns:
        int or float: 매개변수의 타입이 Line클래스가 아닌 경우 0,
                      Line클래스인 경우 s.get_length() ** 2의 결과 값
    Examples:
        >>> figure.area_square(myline)
    """
    if(type(s) != Line):
        return 0
    else:
        return s.get_length() ** 2

def area_circle(s):
    """원의 넓이를 구하는 함수
    Args:
        s: 원의 반지름의 길이
    Returns:
        int or float: 매개변수의 타입이 Line클래스가 아닌 경우 0,
                      Line클래스인 경우 s.get_length() ** 2 * math.pi의 결과 값
    Examples:
        >>> figure.area_circle(myline)
    """
    if(type(s) != Line):
        return 0
    else:
        return s.get_length() ** 2 * math.pi

def area_regular_triangle(s):
    """정삼각형의 넓이를 구하는 함수
    Args:
        s: 정삼각형의 한 변의 길이
    Returns:
        int or float: 매개변수의 타입이 Line클래스가 아닌 경우 0,
                      Line클래스인 경우 s.get_length() ** 2 * math.sqrt(3) / 4의 결과 값
    Examples:
        >>> figure.area_regular_triangle(myline)
    """
    if(type(s) != Line):
        return 0
    else:
        return s.get_length() ** 2 * math.sqrt(3) / 4