from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from src.database.models import Contact, User
from src.schemas.contacts import ContactSchema, ContactUpdateSchema


async def get_contacts(limit: int, offset: int, db: AsyncSession, user: User):
    
    """
        get_contacts
    
        :param limit
        :type limit: int
        :param offset
        :type offset: int
       
        
    """
    sq = select(Contact).filter_by(user=user).offset(offset).limit(limit)
    
    contacts = await db.execute(sq)
    return contacts.scalar().all()


async def get_all_contacts(limit: int, offset: int, db: AsyncSession):
    
    """
        get_all_contacts
    
        :param limit
        :type limit: int
        :param offset
        :type offset: int
       
        
    """
    sq = select(Contact).offset(offset).limit(limit)
    
    contacts = await db.execute(sq)
    return contacts.scalar().all()
    

async def get_contact(contact_id: int, db: AsyncSession, user: User):
    sq = select(Contact).filter_by(id=contact_id, user=User)
    
    contact = await db.execute(sq)
    return contact.scalar_one_or_none()
    

async def create_todo(body: ContactSchema, db: AsyncSession, user: User):
    contact = Contact(**body.model_dump(exclude_unset=True), user=user)
    db.add(contact)
    await db.commit()
    await db.refresh(contact)
    
    return contact


async def update_contact(contact_id: int, body: ContactUpdateSchema, db: AsyncSession, user: User):
    sq = select(Contact).filter_by(id=contact_id, user=user)
       
    upcontact = await db.execute(sq)
    contact = upcontact.scalar_one_or_none()
    if contact:
        contact.first_name = body.first_name
        contact.last_name = body.last_name
        contact.email = body.email
        contact.phone_number = body.phone_number
        contact.birthday = body.birthday
        contact.data = body.data
        await db.commit()
        await db.refresh(contact)
    
    return contact

async def remove_contact(contact_id: int, db: AsyncSession, user: User):
    sq = select(Contact).filter_by(id=contact_id, user=user)
       
    remcontact = await db.execute(sq)
    contact = remcontact.scalar_one_or_none()
    if contact:
        await db.delete(contact)
        await db.commit()
        
    return contact