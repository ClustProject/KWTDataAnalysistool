# KWTDataAnalysistool

특정 시리얼넘버 및 날짜에 대한 공기질측정데이터를 다운로드하여 원하는 시간 단위로 평균하여 출력해주는 전처리 모듈
***
### **HOW TO USE**

1. Load MetaDAta
   
    + 측정기의 시리얼넘버, 시작일, 종료일을 포함하는 메타데이터를 불러옵니다.

2. Data Download
   
    + 메타데이터에 따라 공기질측정데이터를 다운로드합니다.
  
    + 메타데이터 양식이 맞지 않으면 데이터가 다운로드 되지 않습니다.

    ※ 샘플 양식에 맞춰 다시 진행하시면 됩니다.
   
    + 메타데이터가 비어있어도 다운로드 되지 않습니다.
      
    + 각 시리얼넘버에 따라 파일명이 생성됩니다.

3. Average
   
    + Hour Average, Daily Average, Weekly Average 중에 원하는 시간단위의 평균을 진행합니다.
   ![image](https://github.com/ClustProject/KWTDataAnalysistool/assets/136304903/00307e78-63e1-487b-82a8-d66e825036d6)

    + 시리얼넘버-선택시간단위 형태로 파일명이 생성됩니다.
      
    + Weekly Average의 경우, 해당 주중 미세먼지 및 초미세먼지의 최대값과 최소값 정보가 추가컬럼으로 생성됩니다.
   
