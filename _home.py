import streamlit as st

st.title('Euroleague 2024-2025 Stats' )
''
st.subheader('1-Team Comparison')
#htp0='https://raw.githubusercontent.com/ozgurdugmeci/easy-app/main/media/model4.jpg'
biry= '- Select the teams you want to compare. <br> Analyse radar graph for an easy comparision.<br Overview the average team stats' tables. '

st.markdown(biry,unsafe_allow_html=True)
   

img1 ='https://raw.githubusercontent.com/ozgurdugmeci/deneme/main/comparison.jpg'
st.image(img1,width=500)

st.subheader('2-Finished Game Analysis & Productive5')

biry= '- Select the team and choose the game. <br> Analyse radar graph of the two teams.<br> Overview the stats and the game summary of the productive5.'

st.markdown(biry,unsafe_allow_html=True)

img2 ='https://raw.githubusercontent.com/ozgurdugmeci/deneme/main/game_analysis1.jpg'
st.image(img2,width=500)
img3 ='https://raw.githubusercontent.com/ozgurdugmeci/deneme/main/game_analysis2.jpg'
st.image(img3,width=500)


st.subheader('3-Player Stats')
img3 ='https://raw.githubusercontent.com/ozgurdugmeci/deneme/main/player_stats.jpg'
st.image(img3,width=500)
