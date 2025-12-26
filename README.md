<img width="937" height="457" alt="image" src="https://github.com/user-attachments/assets/bd0f279a-8971-4634-b5b7-1b27ef523fbd" />
https://drive.google.com/file/d/1uBtOTszwnLHTDQ0sG14ge8jkioZ3Vc2Z/view?usp=sharing
# Voice-Based Hindi Government Scheme Agent

## Objective
This project implements a voice-first, agentic AI system in Hindi that helps users identify and apply for Indian government welfare schemes.

The system goes beyond a chatbot by using:
- Planning
- Tool execution
- Memory
- Failure handling

## Language
Hindi (End-to-end: Speech → Reasoning → Speech)

## Architecture
- Voice Input (Microphone)
- Speech-to-Text (Whisper)
- Agent Core (Planner–Executor–Evaluator)
- Tools (Eligibility Engine, Scheme Data)
- Memory (Conversation context)
- Text-to-Speech (Hindi voice)
- Streamlit UI (UI only)

## Agent Workflow
1. User speaks in Hindi
2. STT converts voice to text
3. Planner decides next action
4. Executor calls tools
5. Evaluator checks success/failure
6. Agent responds in Hindi voice
7. Memory persists across turns

## Tools Used
- Eligibility Engine (JSON-based rules)
- Scheme Knowledge Base (`schemes.json`)
- Speech-to-Text
- Text-to-Speech

## Failure Handling
- Asks again if age/income missing
- Handles unclear speech
- Resolves contradictory inputs
