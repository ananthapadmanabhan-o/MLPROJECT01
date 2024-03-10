import streamlit as st
from src.pipeline.predict_pipeline import CustomData,PredictPipeline


st.header("Maths Score Predictor") 


gender = st.radio("Select Gender: ", ('male', 'female'))

race_ethnicity = st.selectbox('Select Race/Ethnicity: ',['group A','group B', 'group C' , 'group D', 'group E'])

parental_level_of_education = st.selectbox("Select Parents Education: ",["bachelor's degree", 'some college', "master's degree" ,"associate's degree",'high school' ,'some high school'])

lunch = st.radio('Select lunch',['standard','free/reduced'])

test_preparation_course = st.radio('Select Course',['none','completed'])

reading_score = st.slider('Input Reading Score',min_value=0,max_value=100)

writing_score = st.slider('Input Writing Score',min_value=0,max_value=100)



data = CustomData(
    gender=gender,
    race_ethnicity=race_ethnicity,
    parental_level_of_education=parental_level_of_education,
    lunch=lunch,
    test_preparation_course=test_preparation_course,
    reading_score=reading_score,
    writing_score=writing_score
)

result = 0

st.write('hello')
if (st.button("Predict")):

    predict_df = data.get_data_as_data_frame()
    predict_pipeline = PredictPipeline()
    result = int(predict_pipeline.predict(predict_df))


st.header("Your Maths Score") 
st.header(result) 


