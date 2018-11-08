#ifndef _KS_MODELS_H_
#define _KS_MODELS_H_

#include <string>
#include <vector>
#include <map>
#include <array>


namespace ks
{

#ifndef _KS_OBJECT_
#define _KS_OBJECT_

class KSObject
{
public:
	static inline const std::string nameStatic() { return ""; }
	virtual inline const std::string name() const = 0;
	virtual std::string serialize() const = 0;
	virtual unsigned int deserialize(const std::string &, unsigned int = 0) = 0;
};

#endif // _KS_OBJECT_


namespace models
{

enum class ECell
{
	Empty = 0,
	Food = 1,
	SuperFood = 2,
	Wall = 3,
};


enum class EDirection
{
	Up = 0,
	Right = 1,
	Down = 2,
	Left = 3,
};


class Constants : public KSObject
{

protected:

	int __food_score;
	int __super_food_score;
	int __ghost_death_score;
	int __pacman_death_score;
	int __pacman_max_health;
	int __pacman_giant_form_duration;
	int __max_cycles;

	bool __has_food_score;
	bool __has_super_food_score;
	bool __has_ghost_death_score;
	bool __has_pacman_death_score;
	bool __has_pacman_max_health;
	bool __has_pacman_giant_form_duration;
	bool __has_max_cycles;


public: // getters

	inline int food_score() const
	{
		return __food_score;
	}
	
	inline int super_food_score() const
	{
		return __super_food_score;
	}
	
	inline int ghost_death_score() const
	{
		return __ghost_death_score;
	}
	
	inline int pacman_death_score() const
	{
		return __pacman_death_score;
	}
	
	inline int pacman_max_health() const
	{
		return __pacman_max_health;
	}
	
	inline int pacman_giant_form_duration() const
	{
		return __pacman_giant_form_duration;
	}
	
	inline int max_cycles() const
	{
		return __max_cycles;
	}
	

public: // reference getters

	inline int &ref_food_score() const
	{
		return (int&) __food_score;
	}
	
	inline int &ref_super_food_score() const
	{
		return (int&) __super_food_score;
	}
	
	inline int &ref_ghost_death_score() const
	{
		return (int&) __ghost_death_score;
	}
	
	inline int &ref_pacman_death_score() const
	{
		return (int&) __pacman_death_score;
	}
	
	inline int &ref_pacman_max_health() const
	{
		return (int&) __pacman_max_health;
	}
	
	inline int &ref_pacman_giant_form_duration() const
	{
		return (int&) __pacman_giant_form_duration;
	}
	
	inline int &ref_max_cycles() const
	{
		return (int&) __max_cycles;
	}
	

public: // setters

	inline void food_score(const int &food_score)
	{
		__food_score = food_score;
		has_food_score(true);
	}
	
	inline void super_food_score(const int &super_food_score)
	{
		__super_food_score = super_food_score;
		has_super_food_score(true);
	}
	
	inline void ghost_death_score(const int &ghost_death_score)
	{
		__ghost_death_score = ghost_death_score;
		has_ghost_death_score(true);
	}
	
	inline void pacman_death_score(const int &pacman_death_score)
	{
		__pacman_death_score = pacman_death_score;
		has_pacman_death_score(true);
	}
	
	inline void pacman_max_health(const int &pacman_max_health)
	{
		__pacman_max_health = pacman_max_health;
		has_pacman_max_health(true);
	}
	
	inline void pacman_giant_form_duration(const int &pacman_giant_form_duration)
	{
		__pacman_giant_form_duration = pacman_giant_form_duration;
		has_pacman_giant_form_duration(true);
	}
	
	inline void max_cycles(const int &max_cycles)
	{
		__max_cycles = max_cycles;
		has_max_cycles(true);
	}
	

public: // has_attribute getters

	inline bool has_food_score() const
	{
		return __has_food_score;
	}
	
	inline bool has_super_food_score() const
	{
		return __has_super_food_score;
	}
	
	inline bool has_ghost_death_score() const
	{
		return __has_ghost_death_score;
	}
	
	inline bool has_pacman_death_score() const
	{
		return __has_pacman_death_score;
	}
	
	inline bool has_pacman_max_health() const
	{
		return __has_pacman_max_health;
	}
	
	inline bool has_pacman_giant_form_duration() const
	{
		return __has_pacman_giant_form_duration;
	}
	
	inline bool has_max_cycles() const
	{
		return __has_max_cycles;
	}
	

public: // has_attribute setters

	inline void has_food_score(const bool &has_food_score)
	{
		__has_food_score = has_food_score;
	}
	
	inline void has_super_food_score(const bool &has_super_food_score)
	{
		__has_super_food_score = has_super_food_score;
	}
	
	inline void has_ghost_death_score(const bool &has_ghost_death_score)
	{
		__has_ghost_death_score = has_ghost_death_score;
	}
	
	inline void has_pacman_death_score(const bool &has_pacman_death_score)
	{
		__has_pacman_death_score = has_pacman_death_score;
	}
	
	inline void has_pacman_max_health(const bool &has_pacman_max_health)
	{
		__has_pacman_max_health = has_pacman_max_health;
	}
	
	inline void has_pacman_giant_form_duration(const bool &has_pacman_giant_form_duration)
	{
		__has_pacman_giant_form_duration = has_pacman_giant_form_duration;
	}
	
	inline void has_max_cycles(const bool &has_max_cycles)
	{
		__has_max_cycles = has_max_cycles;
	}
	

public:

	Constants()
	{
		has_food_score(false);
		has_super_food_score(false);
		has_ghost_death_score(false);
		has_pacman_death_score(false);
		has_pacman_max_health(false);
		has_pacman_giant_form_duration(false);
		has_max_cycles(false);
	}
	
	static inline const std::string nameStatic()
	{
		return "Constants";
	}
	
	virtual inline const std::string name() const
	{
		return "Constants";
	}
	
	std::string serialize() const
	{
		std::string s = "";
		
		// serialize food_score
		s += __has_food_score;
		if (__has_food_score)
		{
			int tmp1 = __food_score;
			auto tmp2 = reinterpret_cast<char*>(&tmp1);
			s += std::string(tmp2, sizeof(int));
		}
		
		// serialize super_food_score
		s += __has_super_food_score;
		if (__has_super_food_score)
		{
			int tmp4 = __super_food_score;
			auto tmp5 = reinterpret_cast<char*>(&tmp4);
			s += std::string(tmp5, sizeof(int));
		}
		
		// serialize ghost_death_score
		s += __has_ghost_death_score;
		if (__has_ghost_death_score)
		{
			int tmp7 = __ghost_death_score;
			auto tmp8 = reinterpret_cast<char*>(&tmp7);
			s += std::string(tmp8, sizeof(int));
		}
		
		// serialize pacman_death_score
		s += __has_pacman_death_score;
		if (__has_pacman_death_score)
		{
			int tmp10 = __pacman_death_score;
			auto tmp11 = reinterpret_cast<char*>(&tmp10);
			s += std::string(tmp11, sizeof(int));
		}
		
		// serialize pacman_max_health
		s += __has_pacman_max_health;
		if (__has_pacman_max_health)
		{
			int tmp13 = __pacman_max_health;
			auto tmp14 = reinterpret_cast<char*>(&tmp13);
			s += std::string(tmp14, sizeof(int));
		}
		
		// serialize pacman_giant_form_duration
		s += __has_pacman_giant_form_duration;
		if (__has_pacman_giant_form_duration)
		{
			int tmp16 = __pacman_giant_form_duration;
			auto tmp17 = reinterpret_cast<char*>(&tmp16);
			s += std::string(tmp17, sizeof(int));
		}
		
		// serialize max_cycles
		s += __has_max_cycles;
		if (__has_max_cycles)
		{
			int tmp19 = __max_cycles;
			auto tmp20 = reinterpret_cast<char*>(&tmp19);
			s += std::string(tmp20, sizeof(int));
		}
		
		return s;
	}
	
	unsigned int deserialize(const std::string &s, unsigned int offset=0)
	{
		// deserialize food_score
		__has_food_score = *((unsigned char*) (&s[offset]));
		offset += sizeof(unsigned char);
		if (__has_food_score)
		{
			__food_score = *((int*) (&s[offset]));
			offset += sizeof(int);
		}
		
		// deserialize super_food_score
		__has_super_food_score = *((unsigned char*) (&s[offset]));
		offset += sizeof(unsigned char);
		if (__has_super_food_score)
		{
			__super_food_score = *((int*) (&s[offset]));
			offset += sizeof(int);
		}
		
		// deserialize ghost_death_score
		__has_ghost_death_score = *((unsigned char*) (&s[offset]));
		offset += sizeof(unsigned char);
		if (__has_ghost_death_score)
		{
			__ghost_death_score = *((int*) (&s[offset]));
			offset += sizeof(int);
		}
		
		// deserialize pacman_death_score
		__has_pacman_death_score = *((unsigned char*) (&s[offset]));
		offset += sizeof(unsigned char);
		if (__has_pacman_death_score)
		{
			__pacman_death_score = *((int*) (&s[offset]));
			offset += sizeof(int);
		}
		
		// deserialize pacman_max_health
		__has_pacman_max_health = *((unsigned char*) (&s[offset]));
		offset += sizeof(unsigned char);
		if (__has_pacman_max_health)
		{
			__pacman_max_health = *((int*) (&s[offset]));
			offset += sizeof(int);
		}
		
		// deserialize pacman_giant_form_duration
		__has_pacman_giant_form_duration = *((unsigned char*) (&s[offset]));
		offset += sizeof(unsigned char);
		if (__has_pacman_giant_form_duration)
		{
			__pacman_giant_form_duration = *((int*) (&s[offset]));
			offset += sizeof(int);
		}
		
		// deserialize max_cycles
		__has_max_cycles = *((unsigned char*) (&s[offset]));
		offset += sizeof(unsigned char);
		if (__has_max_cycles)
		{
			__max_cycles = *((int*) (&s[offset]));
			offset += sizeof(int);
		}
		
		return offset;
	}
};


class Pacman : public KSObject
{

protected:

	int __x;
	int __y;
	EDirection __direction;
	int __health;
	int __giant_form_remaining_time;

	bool __has_x;
	bool __has_y;
	bool __has_direction;
	bool __has_health;
	bool __has_giant_form_remaining_time;


public: // getters

	inline int x() const
	{
		return __x;
	}
	
	inline int y() const
	{
		return __y;
	}
	
	inline EDirection direction() const
	{
		return __direction;
	}
	
	inline int health() const
	{
		return __health;
	}
	
	inline int giant_form_remaining_time() const
	{
		return __giant_form_remaining_time;
	}
	

public: // reference getters

	inline int &ref_x() const
	{
		return (int&) __x;
	}
	
	inline int &ref_y() const
	{
		return (int&) __y;
	}
	
	inline EDirection &ref_direction() const
	{
		return (EDirection&) __direction;
	}
	
	inline int &ref_health() const
	{
		return (int&) __health;
	}
	
	inline int &ref_giant_form_remaining_time() const
	{
		return (int&) __giant_form_remaining_time;
	}
	

public: // setters

	inline void x(const int &x)
	{
		__x = x;
		has_x(true);
	}
	
	inline void y(const int &y)
	{
		__y = y;
		has_y(true);
	}
	
	inline void direction(const EDirection &direction)
	{
		__direction = direction;
		has_direction(true);
	}
	
	inline void health(const int &health)
	{
		__health = health;
		has_health(true);
	}
	
	inline void giant_form_remaining_time(const int &giant_form_remaining_time)
	{
		__giant_form_remaining_time = giant_form_remaining_time;
		has_giant_form_remaining_time(true);
	}
	

public: // has_attribute getters

	inline bool has_x() const
	{
		return __has_x;
	}
	
	inline bool has_y() const
	{
		return __has_y;
	}
	
	inline bool has_direction() const
	{
		return __has_direction;
	}
	
	inline bool has_health() const
	{
		return __has_health;
	}
	
	inline bool has_giant_form_remaining_time() const
	{
		return __has_giant_form_remaining_time;
	}
	

public: // has_attribute setters

	inline void has_x(const bool &has_x)
	{
		__has_x = has_x;
	}
	
	inline void has_y(const bool &has_y)
	{
		__has_y = has_y;
	}
	
	inline void has_direction(const bool &has_direction)
	{
		__has_direction = has_direction;
	}
	
	inline void has_health(const bool &has_health)
	{
		__has_health = has_health;
	}
	
	inline void has_giant_form_remaining_time(const bool &has_giant_form_remaining_time)
	{
		__has_giant_form_remaining_time = has_giant_form_remaining_time;
	}
	

public:

	Pacman()
	{
		has_x(false);
		has_y(false);
		has_direction(false);
		has_health(false);
		has_giant_form_remaining_time(false);
	}
	
	static inline const std::string nameStatic()
	{
		return "Pacman";
	}
	
	virtual inline const std::string name() const
	{
		return "Pacman";
	}
	
	std::string serialize() const
	{
		std::string s = "";
		
		// serialize x
		s += __has_x;
		if (__has_x)
		{
			int tmp22 = __x;
			auto tmp23 = reinterpret_cast<char*>(&tmp22);
			s += std::string(tmp23, sizeof(int));
		}
		
		// serialize y
		s += __has_y;
		if (__has_y)
		{
			int tmp25 = __y;
			auto tmp26 = reinterpret_cast<char*>(&tmp25);
			s += std::string(tmp26, sizeof(int));
		}
		
		// serialize direction
		s += __has_direction;
		if (__has_direction)
		{
			char tmp28 = (char) __direction;
			auto tmp29 = reinterpret_cast<char*>(&tmp28);
			s += std::string(tmp29, sizeof(char));
		}
		
		// serialize health
		s += __has_health;
		if (__has_health)
		{
			int tmp31 = __health;
			auto tmp32 = reinterpret_cast<char*>(&tmp31);
			s += std::string(tmp32, sizeof(int));
		}
		
		// serialize giant_form_remaining_time
		s += __has_giant_form_remaining_time;
		if (__has_giant_form_remaining_time)
		{
			int tmp34 = __giant_form_remaining_time;
			auto tmp35 = reinterpret_cast<char*>(&tmp34);
			s += std::string(tmp35, sizeof(int));
		}
		
		return s;
	}
	
	unsigned int deserialize(const std::string &s, unsigned int offset=0)
	{
		// deserialize x
		__has_x = *((unsigned char*) (&s[offset]));
		offset += sizeof(unsigned char);
		if (__has_x)
		{
			__x = *((int*) (&s[offset]));
			offset += sizeof(int);
		}
		
		// deserialize y
		__has_y = *((unsigned char*) (&s[offset]));
		offset += sizeof(unsigned char);
		if (__has_y)
		{
			__y = *((int*) (&s[offset]));
			offset += sizeof(int);
		}
		
		// deserialize direction
		__has_direction = *((unsigned char*) (&s[offset]));
		offset += sizeof(unsigned char);
		if (__has_direction)
		{
			char tmp36;
			tmp36 = *((char*) (&s[offset]));
			offset += sizeof(char);
			__direction = (EDirection) tmp36;
		}
		
		// deserialize health
		__has_health = *((unsigned char*) (&s[offset]));
		offset += sizeof(unsigned char);
		if (__has_health)
		{
			__health = *((int*) (&s[offset]));
			offset += sizeof(int);
		}
		
		// deserialize giant_form_remaining_time
		__has_giant_form_remaining_time = *((unsigned char*) (&s[offset]));
		offset += sizeof(unsigned char);
		if (__has_giant_form_remaining_time)
		{
			__giant_form_remaining_time = *((int*) (&s[offset]));
			offset += sizeof(int);
		}
		
		return offset;
	}
};


class Ghost : public KSObject
{

protected:

	int __id;
	int __x;
	int __y;
	EDirection __direction;

	bool __has_id;
	bool __has_x;
	bool __has_y;
	bool __has_direction;


public: // getters

	inline int id() const
	{
		return __id;
	}
	
	inline int x() const
	{
		return __x;
	}
	
	inline int y() const
	{
		return __y;
	}
	
	inline EDirection direction() const
	{
		return __direction;
	}
	

public: // reference getters

	inline int &ref_id() const
	{
		return (int&) __id;
	}
	
	inline int &ref_x() const
	{
		return (int&) __x;
	}
	
	inline int &ref_y() const
	{
		return (int&) __y;
	}
	
	inline EDirection &ref_direction() const
	{
		return (EDirection&) __direction;
	}
	

public: // setters

	inline void id(const int &id)
	{
		__id = id;
		has_id(true);
	}
	
	inline void x(const int &x)
	{
		__x = x;
		has_x(true);
	}
	
	inline void y(const int &y)
	{
		__y = y;
		has_y(true);
	}
	
	inline void direction(const EDirection &direction)
	{
		__direction = direction;
		has_direction(true);
	}
	

public: // has_attribute getters

	inline bool has_id() const
	{
		return __has_id;
	}
	
	inline bool has_x() const
	{
		return __has_x;
	}
	
	inline bool has_y() const
	{
		return __has_y;
	}
	
	inline bool has_direction() const
	{
		return __has_direction;
	}
	

public: // has_attribute setters

	inline void has_id(const bool &has_id)
	{
		__has_id = has_id;
	}
	
	inline void has_x(const bool &has_x)
	{
		__has_x = has_x;
	}
	
	inline void has_y(const bool &has_y)
	{
		__has_y = has_y;
	}
	
	inline void has_direction(const bool &has_direction)
	{
		__has_direction = has_direction;
	}
	

public:

	Ghost()
	{
		has_id(false);
		has_x(false);
		has_y(false);
		has_direction(false);
	}
	
	static inline const std::string nameStatic()
	{
		return "Ghost";
	}
	
	virtual inline const std::string name() const
	{
		return "Ghost";
	}
	
	std::string serialize() const
	{
		std::string s = "";
		
		// serialize id
		s += __has_id;
		if (__has_id)
		{
			int tmp38 = __id;
			auto tmp39 = reinterpret_cast<char*>(&tmp38);
			s += std::string(tmp39, sizeof(int));
		}
		
		// serialize x
		s += __has_x;
		if (__has_x)
		{
			int tmp41 = __x;
			auto tmp42 = reinterpret_cast<char*>(&tmp41);
			s += std::string(tmp42, sizeof(int));
		}
		
		// serialize y
		s += __has_y;
		if (__has_y)
		{
			int tmp44 = __y;
			auto tmp45 = reinterpret_cast<char*>(&tmp44);
			s += std::string(tmp45, sizeof(int));
		}
		
		// serialize direction
		s += __has_direction;
		if (__has_direction)
		{
			char tmp47 = (char) __direction;
			auto tmp48 = reinterpret_cast<char*>(&tmp47);
			s += std::string(tmp48, sizeof(char));
		}
		
		return s;
	}
	
	unsigned int deserialize(const std::string &s, unsigned int offset=0)
	{
		// deserialize id
		__has_id = *((unsigned char*) (&s[offset]));
		offset += sizeof(unsigned char);
		if (__has_id)
		{
			__id = *((int*) (&s[offset]));
			offset += sizeof(int);
		}
		
		// deserialize x
		__has_x = *((unsigned char*) (&s[offset]));
		offset += sizeof(unsigned char);
		if (__has_x)
		{
			__x = *((int*) (&s[offset]));
			offset += sizeof(int);
		}
		
		// deserialize y
		__has_y = *((unsigned char*) (&s[offset]));
		offset += sizeof(unsigned char);
		if (__has_y)
		{
			__y = *((int*) (&s[offset]));
			offset += sizeof(int);
		}
		
		// deserialize direction
		__has_direction = *((unsigned char*) (&s[offset]));
		offset += sizeof(unsigned char);
		if (__has_direction)
		{
			char tmp49;
			tmp49 = *((char*) (&s[offset]));
			offset += sizeof(char);
			__direction = (EDirection) tmp49;
		}
		
		return offset;
	}
};


class World : public KSObject
{

protected:

	int __width;
	int __height;
	std::vector<std::vector<ECell>> __board;
	std::map<std::string, int> __scores;
	Pacman __pacman;
	std::vector<Ghost> __ghosts;
	Constants __constants;

	bool __has_width;
	bool __has_height;
	bool __has_board;
	bool __has_scores;
	bool __has_pacman;
	bool __has_ghosts;
	bool __has_constants;


public: // getters

	inline int width() const
	{
		return __width;
	}
	
	inline int height() const
	{
		return __height;
	}
	
	inline std::vector<std::vector<ECell>> board() const
	{
		return __board;
	}
	
	inline std::map<std::string, int> scores() const
	{
		return __scores;
	}
	
	inline Pacman pacman() const
	{
		return __pacman;
	}
	
	inline std::vector<Ghost> ghosts() const
	{
		return __ghosts;
	}
	
	inline Constants constants() const
	{
		return __constants;
	}
	

public: // reference getters

	inline int &ref_width() const
	{
		return (int&) __width;
	}
	
	inline int &ref_height() const
	{
		return (int&) __height;
	}
	
	inline std::vector<std::vector<ECell>> &ref_board() const
	{
		return (std::vector<std::vector<ECell>>&) __board;
	}
	
	inline std::map<std::string, int> &ref_scores() const
	{
		return (std::map<std::string, int>&) __scores;
	}
	
	inline Pacman &ref_pacman() const
	{
		return (Pacman&) __pacman;
	}
	
	inline std::vector<Ghost> &ref_ghosts() const
	{
		return (std::vector<Ghost>&) __ghosts;
	}
	
	inline Constants &ref_constants() const
	{
		return (Constants&) __constants;
	}
	

public: // setters

	inline void width(const int &width)
	{
		__width = width;
		has_width(true);
	}
	
	inline void height(const int &height)
	{
		__height = height;
		has_height(true);
	}
	
	inline void board(const std::vector<std::vector<ECell>> &board)
	{
		__board = board;
		has_board(true);
	}
	
	inline void scores(const std::map<std::string, int> &scores)
	{
		__scores = scores;
		has_scores(true);
	}
	
	inline void pacman(const Pacman &pacman)
	{
		__pacman = pacman;
		has_pacman(true);
	}
	
	inline void ghosts(const std::vector<Ghost> &ghosts)
	{
		__ghosts = ghosts;
		has_ghosts(true);
	}
	
	inline void constants(const Constants &constants)
	{
		__constants = constants;
		has_constants(true);
	}
	

public: // has_attribute getters

	inline bool has_width() const
	{
		return __has_width;
	}
	
	inline bool has_height() const
	{
		return __has_height;
	}
	
	inline bool has_board() const
	{
		return __has_board;
	}
	
	inline bool has_scores() const
	{
		return __has_scores;
	}
	
	inline bool has_pacman() const
	{
		return __has_pacman;
	}
	
	inline bool has_ghosts() const
	{
		return __has_ghosts;
	}
	
	inline bool has_constants() const
	{
		return __has_constants;
	}
	

public: // has_attribute setters

	inline void has_width(const bool &has_width)
	{
		__has_width = has_width;
	}
	
	inline void has_height(const bool &has_height)
	{
		__has_height = has_height;
	}
	
	inline void has_board(const bool &has_board)
	{
		__has_board = has_board;
	}
	
	inline void has_scores(const bool &has_scores)
	{
		__has_scores = has_scores;
	}
	
	inline void has_pacman(const bool &has_pacman)
	{
		__has_pacman = has_pacman;
	}
	
	inline void has_ghosts(const bool &has_ghosts)
	{
		__has_ghosts = has_ghosts;
	}
	
	inline void has_constants(const bool &has_constants)
	{
		__has_constants = has_constants;
	}
	

public:

	World()
	{
		has_width(false);
		has_height(false);
		has_board(false);
		has_scores(false);
		has_pacman(false);
		has_ghosts(false);
		has_constants(false);
	}
	
	static inline const std::string nameStatic()
	{
		return "World";
	}
	
	virtual inline const std::string name() const
	{
		return "World";
	}
	
	std::string serialize() const
	{
		std::string s = "";
		
		// serialize width
		s += __has_width;
		if (__has_width)
		{
			int tmp51 = __width;
			auto tmp52 = reinterpret_cast<char*>(&tmp51);
			s += std::string(tmp52, sizeof(int));
		}
		
		// serialize height
		s += __has_height;
		if (__has_height)
		{
			int tmp54 = __height;
			auto tmp55 = reinterpret_cast<char*>(&tmp54);
			s += std::string(tmp55, sizeof(int));
		}
		
		// serialize board
		s += __has_board;
		if (__has_board)
		{
			std::string tmp56 = "";
			unsigned int tmp58 = __board.size();
			auto tmp59 = reinterpret_cast<char*>(&tmp58);
			tmp56 += std::string(tmp59, sizeof(unsigned int));
			while (tmp56.size() && tmp56.back() == 0)
				tmp56.pop_back();
			unsigned char tmp61 = tmp56.size();
			auto tmp62 = reinterpret_cast<char*>(&tmp61);
			s += std::string(tmp62, sizeof(unsigned char));
			s += tmp56;
			
			for (auto &tmp63 : __board)
			{
				s += '\x01';
				std::string tmp64 = "";
				unsigned int tmp66 = tmp63.size();
				auto tmp67 = reinterpret_cast<char*>(&tmp66);
				tmp64 += std::string(tmp67, sizeof(unsigned int));
				while (tmp64.size() && tmp64.back() == 0)
					tmp64.pop_back();
				unsigned char tmp69 = tmp64.size();
				auto tmp70 = reinterpret_cast<char*>(&tmp69);
				s += std::string(tmp70, sizeof(unsigned char));
				s += tmp64;
				
				for (auto &tmp71 : tmp63)
				{
					s += '\x01';
					char tmp73 = (char) tmp71;
					auto tmp74 = reinterpret_cast<char*>(&tmp73);
					s += std::string(tmp74, sizeof(char));
				}
			}
		}
		
		// serialize scores
		s += __has_scores;
		if (__has_scores)
		{
			std::string tmp75 = "";
			unsigned int tmp77 = __scores.size();
			auto tmp78 = reinterpret_cast<char*>(&tmp77);
			tmp75 += std::string(tmp78, sizeof(unsigned int));
			while (tmp75.size() && tmp75.back() == 0)
				tmp75.pop_back();
			unsigned char tmp80 = tmp75.size();
			auto tmp81 = reinterpret_cast<char*>(&tmp80);
			s += std::string(tmp81, sizeof(unsigned char));
			s += tmp75;
			
			for (auto &tmp82 : __scores)
			{
				s += '\x01';
				std::string tmp83 = "";
				unsigned int tmp85 = tmp82.first.size();
				auto tmp86 = reinterpret_cast<char*>(&tmp85);
				tmp83 += std::string(tmp86, sizeof(unsigned int));
				while (tmp83.size() && tmp83.back() == 0)
					tmp83.pop_back();
				unsigned char tmp88 = tmp83.size();
				auto tmp89 = reinterpret_cast<char*>(&tmp88);
				s += std::string(tmp89, sizeof(unsigned char));
				s += tmp83;
				
				s += tmp82.first;
				
				s += '\x01';
				int tmp91 = tmp82.second;
				auto tmp92 = reinterpret_cast<char*>(&tmp91);
				s += std::string(tmp92, sizeof(int));
			}
		}
		
		// serialize pacman
		s += __has_pacman;
		if (__has_pacman)
		{
			s += __pacman.serialize();
		}
		
		// serialize ghosts
		s += __has_ghosts;
		if (__has_ghosts)
		{
			std::string tmp93 = "";
			unsigned int tmp95 = __ghosts.size();
			auto tmp96 = reinterpret_cast<char*>(&tmp95);
			tmp93 += std::string(tmp96, sizeof(unsigned int));
			while (tmp93.size() && tmp93.back() == 0)
				tmp93.pop_back();
			unsigned char tmp98 = tmp93.size();
			auto tmp99 = reinterpret_cast<char*>(&tmp98);
			s += std::string(tmp99, sizeof(unsigned char));
			s += tmp93;
			
			for (auto &tmp100 : __ghosts)
			{
				s += '\x01';
				s += tmp100.serialize();
			}
		}
		
		// serialize constants
		s += __has_constants;
		if (__has_constants)
		{
			s += __constants.serialize();
		}
		
		return s;
	}
	
	unsigned int deserialize(const std::string &s, unsigned int offset=0)
	{
		// deserialize width
		__has_width = *((unsigned char*) (&s[offset]));
		offset += sizeof(unsigned char);
		if (__has_width)
		{
			__width = *((int*) (&s[offset]));
			offset += sizeof(int);
		}
		
		// deserialize height
		__has_height = *((unsigned char*) (&s[offset]));
		offset += sizeof(unsigned char);
		if (__has_height)
		{
			__height = *((int*) (&s[offset]));
			offset += sizeof(int);
		}
		
		// deserialize board
		__has_board = *((unsigned char*) (&s[offset]));
		offset += sizeof(unsigned char);
		if (__has_board)
		{
			unsigned char tmp101;
			tmp101 = *((unsigned char*) (&s[offset]));
			offset += sizeof(unsigned char);
			std::string tmp102 = std::string(&s[offset], tmp101);
			offset += tmp101;
			while (tmp102.size() < sizeof(unsigned int))
				tmp102 += '\x00';
			unsigned int tmp103;
			tmp103 = *((unsigned int*) (&tmp102[0]));
			
			__board.clear();
			for (unsigned int tmp104 = 0; tmp104 < tmp103; tmp104++)
			{
				std::vector<ECell> tmp105;
				offset++;
				unsigned char tmp106;
				tmp106 = *((unsigned char*) (&s[offset]));
				offset += sizeof(unsigned char);
				std::string tmp107 = std::string(&s[offset], tmp106);
				offset += tmp106;
				while (tmp107.size() < sizeof(unsigned int))
					tmp107 += '\x00';
				unsigned int tmp108;
				tmp108 = *((unsigned int*) (&tmp107[0]));
				
				tmp105.clear();
				for (unsigned int tmp109 = 0; tmp109 < tmp108; tmp109++)
				{
					ECell tmp110;
					offset++;
					char tmp111;
					tmp111 = *((char*) (&s[offset]));
					offset += sizeof(char);
					tmp110 = (ECell) tmp111;
					tmp105.push_back(tmp110);
				}
				__board.push_back(tmp105);
			}
		}
		
		// deserialize scores
		__has_scores = *((unsigned char*) (&s[offset]));
		offset += sizeof(unsigned char);
		if (__has_scores)
		{
			unsigned char tmp112;
			tmp112 = *((unsigned char*) (&s[offset]));
			offset += sizeof(unsigned char);
			std::string tmp113 = std::string(&s[offset], tmp112);
			offset += tmp112;
			while (tmp113.size() < sizeof(unsigned int))
				tmp113 += '\x00';
			unsigned int tmp114;
			tmp114 = *((unsigned int*) (&tmp113[0]));
			
			__scores.clear();
			for (unsigned int tmp115 = 0; tmp115 < tmp114; tmp115++)
			{
				std::string tmp116;
				offset++;
				unsigned char tmp118;
				tmp118 = *((unsigned char*) (&s[offset]));
				offset += sizeof(unsigned char);
				std::string tmp119 = std::string(&s[offset], tmp118);
				offset += tmp118;
				while (tmp119.size() < sizeof(unsigned int))
					tmp119 += '\x00';
				unsigned int tmp120;
				tmp120 = *((unsigned int*) (&tmp119[0]));
				
				tmp116 = s.substr(offset, tmp120);
				offset += tmp120;
				
				int tmp117;
				offset++;
				tmp117 = *((int*) (&s[offset]));
				offset += sizeof(int);
				
				__scores[tmp116] = tmp117;
			}
		}
		
		// deserialize pacman
		__has_pacman = *((unsigned char*) (&s[offset]));
		offset += sizeof(unsigned char);
		if (__has_pacman)
		{
			offset = __pacman.deserialize(s, offset);
		}
		
		// deserialize ghosts
		__has_ghosts = *((unsigned char*) (&s[offset]));
		offset += sizeof(unsigned char);
		if (__has_ghosts)
		{
			unsigned char tmp121;
			tmp121 = *((unsigned char*) (&s[offset]));
			offset += sizeof(unsigned char);
			std::string tmp122 = std::string(&s[offset], tmp121);
			offset += tmp121;
			while (tmp122.size() < sizeof(unsigned int))
				tmp122 += '\x00';
			unsigned int tmp123;
			tmp123 = *((unsigned int*) (&tmp122[0]));
			
			__ghosts.clear();
			for (unsigned int tmp124 = 0; tmp124 < tmp123; tmp124++)
			{
				Ghost tmp125;
				offset++;
				offset = tmp125.deserialize(s, offset);
				__ghosts.push_back(tmp125);
			}
		}
		
		// deserialize constants
		__has_constants = *((unsigned char*) (&s[offset]));
		offset += sizeof(unsigned char);
		if (__has_constants)
		{
			offset = __constants.deserialize(s, offset);
		}
		
		return offset;
	}
};

} // namespace models

} // namespace ks

#endif // _KS_MODELS_H_
