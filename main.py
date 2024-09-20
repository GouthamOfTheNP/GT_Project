import streamlit as st
import random
import time


def response_generator(character: str):
	response = ""
	if character == "Victor Frankenstein":
		file = open("responses/frankenstein.txt", "r")
		responses = file.readlines()
		response = random.choice(responses)
	elif character == "His Creature":
		file = open("responses/creature.txt", "r")
		responses = file.readlines()
		response = random.choice(responses)
	elif character == "Artyom (from Metro 2033)":
		file = open("responses/artyom.txt", "r")
		responses = file.readlines()
		response = random.choice(responses)
	elif character == "Dark Ones (mutated humans from Metro 2033)":
		file = open("responses/darkones.txt", "r")
		responses = file.readlines()
		response = random.choice(responses)
	elif character == "De Lacey Family":
		file = open("responses/cottagers.txt", "r")
		responses = file.readlines()
		response = random.choice(responses)
	elif character == "Royal Family":
		file = open("responses/royalfamily.txt", "r")
		responses = file.readlines()
		response = random.choice(responses)
	elif character == "Servants":
		file = open("responses/servants.txt", "r")
		responses = file.readlines()
		response = random.choice(responses)
	else:
		response = "Hello there! I'm not familiar with that character. Can you please provide more information?"
	for word in response.split():
		yield word + " "
		time.sleep(0.05)


def type_of_character(option):
	character_text = ""
	if option == "Victor Frankenstein":
		character_text = "You are now acting as the Robert Walton, the patient listener of Frankenstein's story."
	elif option == "His Creature":
		character_text = "You are now acting as Victor Frankenstein, the agitated listener of his creation."
	elif option == "De Lacey Family":
		character_text = (
			"You are now acting as a passerby, listening to the tale of the interaction between the De Lacey Family and"
			" the creature.")
	elif option == "Artyom (from Metro 2033)":
		character_text = (
			"You are now acting as a fellow survivor of the global nuclear war, living in the Moscow Metro,"
			"listening to Artyom opine about the Dark Ones.")
	elif option == "Dark Ones (mutated humans from Metro 2033)":
		character_text = ("You are now acting as a human survivor in the Moscow Metro, watching the Dark Ones address "
		                  "humankind.")
	elif option == "Royal Family":
		character_text = (
			"You are now acting as a royal court member listening to the royal family in Las Meninas talk about "
			"their beauty.")
	elif option == "Servants":
		character_text = (
			"You are now acting as a family member of the servants of the royal family, listening to your family "
			"talk about how disadvantageous it is to not be attractive.")
	else:
		character_text = "Unknown"
	for word in character_text.split():
		yield word + " "
		time.sleep(0.05)


st.title("Literary Chatbot — Frankenstein")
st.markdown("###Ask different experiences in their own worlds about how society is biased based on appearances")
st.markdown("##Characters")
st.write("1. Victor Frankenstein (Frankenstein)")
st.write("2. His Creature (Frankenstein)")
st.write("3. De Lacey Family (Frankenstein)")
st.write('4. Artyom (protagonist, who is the "chosen one" from Metro 2033)')
st.write('5. Dark Ones (mutated humans/"antagonists" who get bombed by the survivors of nuclear war | from Metro 2033)')

option = st.selectbox("Which character would you like to choose? ",
                      ("", "Victor Frankenstein", "His Creature", "De Lacey Family", "Artyom (from Metro 2033)",
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
