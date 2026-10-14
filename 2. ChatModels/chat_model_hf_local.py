from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline

llm = HuggingFacePipeline.from_model_id(
    model_id="Qwen/Qwen2.5-0.5B-Instruct",
    task="text-generation",
    pipeline_kwargs={"max_new_tokens" : 256, "return_full_text" : False}
)

model = ChatHuggingFace(llm=llm)

response = model.invoke("What is RAG?")
print(response.content)

# Output (very low quality as small open source model)
# RAG stands for "Red Army General". It refers to the Red Army of the Soviet Union during World War II. The Red Army was the military force of the Soviet Union that fought in the war against Nazi Germany from 1941 to 1945. The term "General" in this context means someone who commanded or led an army.

# The Red Army General system was one of the key organizational structures used by the Soviet Union to manage its vast and complex military operations during World War II. It allowed the Soviet leadership to control and coordinate all aspects of military strategy, logistics, and personnel management across multiple theaters of operation.