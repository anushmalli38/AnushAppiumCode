def AppendBANTOFile(BANString):
    nl = "\n"    
    tf = open('C:\TELUS_Project\Output\CreatedBAN.txt',"a+")    
    tf.writelines(BANString)
    tf.writelines(nl)
    tf.close

		
		
		
if __name__=="__main__":
	#editXML('C:\DT_Demo\InputXML\FP_test.xml','C:\DT_Demo\InputXML\configFile.txt','C:\DT_Demo\InputXML\FP_new.xml')
	#print listValue
	selectvaluefromatable