import streamlit as st
import pickle

with open('D:\DOWNLOAD\labib\Digital Skola\File Coba2\Random_Forest_Model1.pkl', 'rb') as file:
    Random_Forest_Model = pickle.load(file)
with open('D:\DOWNLOAD\labib\Digital Skola\File Coba2\Random_Forest_Model1.pkl', 'rb') as file:
    model = pickle.load(file)

def main():
    design = """<div style='padding:15px;">
                    <h1 style='color:#fff'>Properti Prediksi</h1>
                </div>"""
    st.markdown(design, unsafe_allow_html=True)
    left, right = st.columns((2,2))
    BHK = left.selectbox('BHK', (1,2,3,4,5,6))
    Area_type = right.selectbox('Area Type', ('Super Area', 'Carpet Area', 'Built Area'))
    City = left.selectbox('City', ('Mumbai', 'Kolkata', 'Bangalore', 'Delhi', 'Chennai', 'Hyderabad'))
    Furnishing_status = right.selectbox('Furnishing Status', ('Unfurnished', 'Semi-Furnished', 'Furnished'))
    Tenant_preferred = left.selectbox('Tenant Preferred',('Bachelors/Family','Bachelors', 'Family'))
    bathdroom = right.selectbox('Bathroom',(1,2,3,4,5,6,7,10))
    Building_Floor =left.number_input('Building Floor')
    #Building_Floor =left.selectbox('Building Floor',(1,2,3,4,5,6,7,8,9,'=>10'))
    Basement_Floor = right.selectbox('Basement Floor', (0,1))
    Size = left.selectbox('Size',('10-500','500-1000','1000-1500','>15O0'))
    Rent = right.number_input('Rent (Rupee)')
    button = st.button('Predict')
    if button :
     #make prediction
        result = predict(BHK,Area_type,Furnishing_status,City, Tenant_preferred, bathdroom,Building_Floor,Basement_Floor, Size, Rent)
        if result == 'Sesuai':
            st.success(f'Properti {result} dengan kriteria')
        else:
            st.warning(f'Properti kurang {result} dengan kriteria')

def predict(BHK,Area_type,Furnishing_status,City, Tenant_preferred, bathdroom,Building_Floor,Basement_Floor, Size, Rent):
    #processing user input

    Areat = 0 if Area_type == 'Super Area'else 1 if Area_type == 'Carpet Area' else 2
    Cy = 0 if City == 'Mumbai' else 1 if City == 'Kolkata' else 2 if City == 'Bangalore' else 3 if City =='Delhi' else 4 if City =='Chennai' else 5
    Fur_status = 0 if Furnishing_status == 'Unfurnished' else 1 if Furnishing_status == 'Semi-Furnished' else 2
    Ten_preferred = 0 if Tenant_preferred == 'Bachelors/Family' else 1 if Tenant_preferred == 'Bachelors' else 2
    Siz = 0 if Size== '10-500' else 1 if Size=='500-1000' else 2 if Size== '1000-1500' else 3 

    #Making prediction
    prediction = Random_Forest_Model.predict([[Areat, Cy, Fur_status, Ten_preferred, Siz]])
    result = 'Tidak Sesuai' if prediction == 0 else 'Sesuai'

    return result

if __name__ == "__main__":
    main()