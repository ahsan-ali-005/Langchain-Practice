from langchain_core.prompts import PromptTemplate


# PromptTemplate provides validation of input, resuable so better than direct f-strings for prompts
template = PromptTemplate(
    template="""
Act as an experienced blog writer, SEO content strategist, and subject-matter expert in {niche}.

Topic:-
- **Topic: {blog_topic}
- **Main Keyword: {primary_keyword}
- **Target Audience: {target_audience}
- **Target Length: {length}

Tone:-
- **Tone: {tone}
- **Writing Style: {writing_style}
- **Personality:** Sound human, helpful, and knowledgeable rather than robotic or overly formal.

Structure:-
1. **SEO Title:** Create a compelling title that includes the primary keyword naturally.
2. **Meta Description:** Write a concise, engaging description of approximately 150–160 characters.
3. **Introduction:** Start with a relatable problem, question, statistic, or hook. Explain what the reader will learn.
4. **Main Content:** Organize the blog into logical H2 and H3 headings. Explain each point clearly and include relevant examples.
5. **Practical Examples:** Use real-world scenarios, actionable tips, or step-by-step instructions where appropriate.
6. **Common Mistakes:** Highlight relevant mistakes and explain how to avoid them.
7. **Conclusion:** Summarize the key takeaways and provide a clear final message.
8. **Call to Action (CTA):** [e.g., Subscribe, Leave a Comment, Explore a Product, Contact Us]

Content Quality Rules
- Provide useful information rather than generic filler.
- Explain complex concepts in simple terms.
- Include specific examples, comparisons, or actionable steps where relevant.
- Avoid repeating the same idea across multiple sections.
- Use bullet points, numbered lists, or tables when they improve readability.
- Make the content original and naturally written.
- Do not force every suggested section into the blog if it does not fit the topic.
- If essential information is missing, ask clarifying questions before writing.


Before finalizing, check that the blog meets the requested word count, tone, style, audience, and SEO requirements.

Now generate the blog post using the details provided above.
"""

    ,
    input_variables=["niche", "blog_topic", "primary_keyword", "target_audience","length", "tone","writing_style"]

)

template.save('prompt_template.json') # create a json template for prompts