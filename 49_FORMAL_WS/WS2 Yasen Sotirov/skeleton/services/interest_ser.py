from data.database import read_query, query_count, insert_query, update_query


def interests_on_category(category_id: int, profile_id: int) -> int:
    return read_query('''SELECT relevance 
                        FROM interests
                        WHERE category_id = ? AND profile_id = ?''',
                      (category_id, profile_id))


def has_interest(category_id: int, profile_id: int):
    result = query_count('''SELECT COUNT(*) FROM interests WHERE category_id = ? AND profile_id = ?''',
                         (category_id, profile_id)) > 0
    return result




def add_interest_on_category(category_id, profile_id):
    insert_query('''INSERT INTO interests (category_id, profile_id, relevance)
                    VALUES(?,?,?)''',(category_id, profile_id, 1))



def increase_interest(relevance, primary_key):
    update_query('''UPDATE interests SET relevance = ?
                    WHERE id = ?''',(relevance, primary_key))








