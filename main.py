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
	elif character == "Cottagers":
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


st.title("Literary Chatbot — Frankenstein")
st.write("Ask different experiences in their own worlds about how society is biased based on appearances")

option = st.selectbox(
	"Which character would you like to choose? ",
	("Victor Frankenstein", "His Creature", "Cottagers", "Artyom (from Metro 2033)",
	 "Dark Ones (mutated humans from Metro 2033)", "Royal Family", "Servants"))
# Initialize chat history
if "messages" not in st.session_state:
	st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
	with st.chat_message(message["role"]):
		st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("What would you like to learn?"):
	# Add user message to chat history
	st.session_state.messages.append({"role": "user", "content": prompt})
	# Display user message in chat message container
	with st.chat_message("user"):
		st.markdown(prompt)

	# Display assistant response in chat message container
	with st.chat_message("assistant"):
		response = st.write_stream(response_generator(option))
	# Add assistant response to chat history
	st.session_state.messages.append({"role": "assistant", "content": response})
