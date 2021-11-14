print("########## 계산기 실행 ##########")

while(1):
	try:
		menu = int(input("1. 덧셈 2. 뺄셈 3. 곱셈 4. 나눗셈 5. 종료 (예: 1): "))
	except:
		print("메뉴를 숫자로 정확하게 입력해주세요.")
	else:

		if (menu == 5):
			print("########## 계산기 종료 ##########")
			break
		elif (menu == 1 or menu == 2 or menu == 3 or menu == 4):
			num = input("두 정수를 입력하시오. (예: 1 4): ")
		
			try:
				n1, n2 = num.split()
				n1 = int(n1)
				n2 = int(n2)
			except:
				print("두 개의 정수를 정확하게 입력해주세요.")
				print("처음으로 돌아갑니다.")
				print("")
			else:
				print("입력한 두 정수는 ", n1, "과", n2, "입니다.")

				if (menu == 1):
					print("덧셈 결과:", n1, "+", n2, "=", n1+n2)
					print("")
				elif (menu == 2):
					print("뺄셈 결과:", n1, "-", n2, "=", n1-n2)
					print("")
				elif (menu == 3):
					print("곱셈 결과:", n1, "*", n2, "=", n1*n2)
					print("")
				elif (menu == 4):
					if (n2 == 0):
						print("나눗셈 결과: 나누는 값이 0이므로 나눗셈이 불가능해 결과값이 없습니다.")
						print("")
					else:
						print("나눗셈 결과:", n1, "/", n2, "=", n1/n2)
						print("")
		else:
			print("해당하는 메뉴가 없습니다.")
			print("메뉴를 다시 입력해주세요.")
			print("")
