import streamlit as st
import random
import time

st.set_page_config(page_title="Literary Exploration Bot — Goutham Pedinedi")

def response_generator(character: str):
	response = ""
	if character == "Victor Frankenstein":
		file = open("responses/frankenstein.txt", "r")
		responses = file.readlines()
		response = "AI: " + random.choice(responses)
	elif character == "Frankenstein's Creature":
		file = open("responses/creature.txt", "r")
		responses = file.readlines()
		response = "AI: " + random.choice(responses)
	elif character == "Artyom (from Metro 2033)":
		file = open("responses/artyom.txt", "r")
		responses = file.readlines()
		response = "AI: " + random.choice(responses)
	elif character == "Dark Ones (mutated humans from Metro 2033)":
		file = open("responses/darkones.txt", "r")
		responses = file.readlines()
		response = "AI: " + random.choice(responses)
	elif character == "De Lacey Family":
		file = open("responses/cottagers.txt", "r")
		responses = file.readlines()
		response = random.choice(responses)
	elif character == "Royal Family":
		file = open("responses/royalfamily.txt", "r")
		responses = file.readlines()
		response = "AI: " + random.choice(responses)
	elif character == "Servants":
		file = open("responses/servants.txt", "r")
		responses = file.readlines()
		response = "AI: " + random.choice(responses)
	else:
		response = "AI: " + "Hello there! I'm not familiar with that character. Can you please provide more information?"
	for word in response.split():
		yield word + " "
		time.sleep(0.05)


def type_of_character(option):
	character_text = ""
	if option == "Victor Frankenstein":
		character_text = "Assistant" + ": " + "You are now acting as the Robert Walton, the patient listener of Frankenstein's story."
	elif option == "Frankenstein's Creature":
		character_text = "Assistant" + ": " + "You are now acting as Victor Frankenstein, the agitated listener of his creation."
	elif option == "De Lacey Family":
		character_text = ("Assistant" + ": " +
			"You are now acting as a passerby, listening to the tale of the interaction between the De Lacey Family and"
			" the creature.")
	elif option == "Artyom (from Metro 2033)":
		character_text = ("Assistant" + ": " +
			"You are now acting as a fellow survivor of the global nuclear war, living in the Moscow Metro,"
			"listening to Artyom opine about the Dark Ones.")
	elif option == "Dark Ones (mutated humans from Metro 2033)":
		character_text = ("Assistant" + ": " + "You are now acting as a human survivor in the Moscow Metro, watching the Dark Ones address "
		                  "humankind.")
	elif option == "Royal Family":
		character_text = ("Assistant" + ": " +
			"You are now acting as a part of the royal family, listening to your family in Las Meninas talk about "
			"their beauty.")
	elif option == "Servants":
		character_text = ("Assistant" + ": " +
			"You are now acting as a family member of the servants of the royal family, listening to your family "
			"talk about how disadvantageous it is to not be attractive.")
	else:
		character_text = "Unknown"
	for word in character_text.split():
		yield word + " "
		time.sleep(0.05)


st.title("Literary Exploration Bot")
st.markdown("### Learn about about different characters' experiences (in their own worlds) about how society is biased "
            "based on appearances")
st.markdown("## Characters")
st.write("1. Victor Frankenstein (Frankenstein)")
st.write("2. Frankenstein's Creature (Frankenstein)")
st.write("3. De Lacey Family (Frankenstein)")
st.write('4. Artyom (protagonist, who is the "chosen one" from Metro 2033)')
st.write('5. Dark Ones (mutated humans/"antagonists" who get bombed by the survivors of nuclear war | from Metro 2033)')
url = "https://en.wikipedia.org/wiki/File:Las_Meninas,_by_Diego_Vel%C3%A1zquez,_from_Prado_in_Google_Earth.jpg"
st.write('6. Royal Family ([Las Meninas](%s))' % url)
st.write('7. Servants ([Las Meninas](%s))' % url)

option = st.selectbox("Which character would you like to choose? ",
                      ("", "Victor Frankenstein", "Frankenstein's Creature", "De Lacey Family", "Artyom (from Metro 2033)",
                       "Dark Ones (mutated humans from Metro 2033)", "Royal Family", "Servants"))

st.session_state.messages = []
for message in st.session_state.messages:
	with st.chat_message(message["role"]):
		st.markdown(message["content"])

# Accept user input
if option != "":
	# Add user message to chat history
	time.sleep(1)
	with st.chat_message("assistant"):
		character = st.write_stream(type_of_character(option))
	# Display user message in chat message container
	# Display assistant response in chat message container
	time.sleep(2)
	with st.chat_message("ai"):
		response = st.write_stream(response_generator(option))
	# Add assistant response to chat history
	st.session_state.messages.append({"role": "assistant", "content": response})

footer = """<style>
a:link , a:visited{
color: blue;
background-color: transparent;
text-decoration: underline;
}

a:hover,  a:active {
color: red;
background-color: transparent;
text-decoration: underline;
}

.footer {
position: dynamic;
left: 0;
bottom: 0;
width: 100%;
text-align: center;
}
</style>
<div class="footer">
<p>Developed with Python and Streamlit by Goutham Pedinedi</p>
</div>
"""
st.markdown(footer, unsafe_allow_html=True)
