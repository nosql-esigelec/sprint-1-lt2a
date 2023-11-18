# app/api/routes/projects.py
import os
from typing import List
from fastapi import APIRouter, HTTPException, Depends
from api.v1.src.models.question import Question
from api.v1.src.models.option import Option
from api.v1.src.models.section import Section
from api.v1.src.dependencies import get_neo4j_db
from api.v1.src.services.sections_service import SectionService

router = APIRouter()
neo4j = get_neo4j_db()
sections_service = SectionService(neo4j)


@router.get("/", response_model=List[Section])
async def get_sections() -> Section:
    sections = sections_service.get_sections()
    if sections is None:
        raise HTTPException(status_code=404, detail="Section not found")
    return sections


# Get section by a specific attibute and his value(id, order, name, etc.)
@router.get("/by/{property}/{value}", response_model=Section)
async def find_section_by_property(
        property: str, value: str
) -> Section:
    section = sections_service.get_section_by_property(property, value)
    if section is None:
        raise HTTPException(status_code=404, detail="Section not found")
    return section


@router.get("/{section_id}/next-section", response_model=Section)
async def get_next_section(section_id: str) -> Section:
    next_section = sections_service.get_next_section(section_id)
    if next_section is None:
        raise HTTPException(status_code=404, detail="Next section not found")
    return next_section


@router.get("/next-questions", response_model=List[Question])
async def get_next_questions(
        question_id: str, option_text: str
) -> List[Question]:
    questions = sections_service.get_next_questions(question_id, option_text)

    if questions is None or len(questions) == 0:
        raise HTTPException(
            status_code=404, detail="Questions for the section not found"
        )
    print(f"Questions to return: {questions}")
    return questions


@router.get("/{section_id}/questions", response_model=List[Question])
async def get_questions_for_section(
        section_id: str
) -> List[Question]:
    questions = sections_service.get_questions_for_section(section_id)

    if questions is None or len(questions) == 0:
        raise HTTPException(
            status_code=404, detail="Questions for the section not found"
        )
    print(f"Questions to return: {questions}")
    return questions