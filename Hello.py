import streamlit as st

st.title("GlobalJava Roasters")

st.sidebar.title('Navigation')
page = st.sidebar.selectbox("Choose a section", ['About Us', 'FAQs', 'Submit Feedback'])


if page == 'Submit Feedback':
    st.header("Customer Feedback Form")
    st.image("https://s3.amazonaws.com/dq-content/900/coffee.jpg")
    st.write("Your input helps us brew a better experience. Please share your thoughts about our coffee and service.")

    answer = st.radio(
        "Did you enjoy your coffee?",
        ['Yes!', 'No'])

    if answer == 'Yes!':
        st.write("Glad you enjoyed it!")
    elif answer == 'No':
        st.write("We're sorry to hear that. We'll strive to improve.")
        
    coffee_rating = st.slider("On a scale of 1 to 10, how would you rate our coffee today?", 1, 10, 5)

    service_type = st.selectbox("What type of service did you experience?", ["In-store", "Online", "Phone"])

    st.write(f"You rated our coffee a {coffee_rating} and experienced {service_type} service.")

    st.write("We value your feedback. Please tell us more about your experience.")
    name = st.text_input("Name")
    message = st.text_area("Feedback")
    st.write(f"Thank you {name} for your feedback: {message}")

    agree = st.checkbox("I agree to the terms and conditions.")






if page == 'About Us':
    st.header('About Us')
    # Add your columns here
    col1, col2, col3 = st.columns(3) 
    cols = [col1, col2, col3]
    
    images = [
    "https://s3.amazonaws.com/dq-content/901/Charles_Bingley.png",
    "https://s3.amazonaws.com/dq-content/901/Elizabeth_Bennet.png",
    "https://s3.amazonaws.com/dq-content/901/Georgiana_Darcy.png"
            ]
    names = ['Elizabeth Bennet', 	'Charles Bingley', 	'Georgiana Darcy']
    texts = ['Founder and CEO, Elizabeth is passionate about bringing customers flavorful and delicious coffee.',
             'Marketing Director and Social Media Expert, Charles helps the world know about our great new flavors!',
             'Georgiana is the creative genius behind the scenes!'
            ]
    
    for i, col in enumerate(cols, start=0):
        with col:
            st.image(images[i])
            st.header(names[i])
            st.write(texts[i])








def general_faqs():
    bean_source_expander = st.expander('Where do you source your coffee beans?')
    with bean_source_expander:
        st.write('Our coffee beans are ethically sourced from family-owned farms and cooperatives across various coffee-growing regions, ensuring quality and sustainability in every cup.')
        
    roast_expander = st.expander('How do you roast your beans?')
    with roast_expander:
        st.write('We employ a combination of traditional and modern roasting techniques, meticulously adjusting the roast profile for each batch to bring out the unique flavors and aromas of the beans.')

# Define your function here
def recipe_faqs():
    cold_brew_expander = st.expander('What is your recommended recipe for a classic cold brew coffee?')
    with cold_brew_expander:
        st.write( 'For a smooth and robust cold brew, mix coarsely ground coffee beans with cold water in a 1:8 ratio, steep for 12-18 hours, and then filter. Serve over ice and customize with milk or sweeteners to taste.')
        
       
    dessert_expander = st.expander( 'Do you have a signature coffee-based dessert recipe?')
    with dessert_expander:
        st.write("Yes, our signature dessert is the 'GlobalJava Mocha Brownies.' Blend melted dark chocolate with your favorite GlobalJava espresso shot, add to your brownie mix, and bake. These rich, coffee-infused brownies are a coffee lover's delight and perfect for any occasion.")
    
if page == 'FAQs':
    st.header('FAQs')
    tab1, tab2 = st.tabs(["General", "Recipes"])
    with tab1:
        general_faqs()
    with tab2:
        recipe_faqs()

    