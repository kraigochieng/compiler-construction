import re

code = """
int myNum = 213;
int myNum2 = 2;
char myLetter = ‘P’;
decimal myDecimal = 9.23;
char checker[100] = “”;
Int myNum3 = 1737; 
char line_break=''
if (myNum > myNum2 && myNum > myNum3) {
	checker = “myNum is greater than myNum2 and myNum3”;
} else if(myNum == myNum2 || myNum == myNum3) {
checker = “myNum is equal to myNum2 or myNum3”;
} else {
	checker = “myNum is less than myNum2”;
}

int j = 0; 
Int k = 1;
Int m = 1000;
float n = 1000; 

for(int i = 0; i < 10; i = i + 1 ) {
	j = j + i;
	k = k * i;
	m = m - i;
	n = n / i;
}
"""

# Replacing line breaks with nothing
#print(code.replace("\n", ""))

# print(re.sub(r'(?<!\\)\s+', '', code))
# print(re.sub(r"(?<!')\\n(?!')", '', code))
print(re.sub(r"\n", "", code))
