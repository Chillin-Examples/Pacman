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

	int __foodScore;
	int __superFoodScore;
	int __ghostDeathScore;
	int __pacmanDeathScore;
	int __pacmanGiantFormDuration;
	int __maxCycles;

	bool __has_foodScore;
	bool __has_superFoodScore;
	bool __has_ghostDeathScore;
	bool __has_pacmanDeathScore;
	bool __has_pacmanGiantFormDuration;
	bool __has_maxCycles;


public: // getters

	inline int foodScore() const
	{
		return __foodScore;
	}
	
	inline int superFoodScore() const
	{
		return __superFoodScore;
	}
	
	inline int ghostDeathScore() const
	{
		return __ghostDeathScore;
	}
	
	inline int pacmanDeathScore() const
	{
		return __pacmanDeathScore;
	}
	
	inline int pacmanGiantFormDuration() const
	{
		return __pacmanGiantFormDuration;
	}
	
	inline int maxCycles() const
	{
		return __maxCycles;
	}
	

public: // reference getters

	inline int &ref_foodScore() const
	{
		return (int&) __foodScore;
	}
	
	inline int &ref_superFoodScore() const
	{
		return (int&) __superFoodScore;
	}
	
	inline int &ref_ghostDeathScore() const
	{
		return (int&) __ghostDeathScore;
	}
	
	inline int &ref_pacmanDeathScore() const
	{
		return (int&) __pacmanDeathScore;
	}
	
	inline int &ref_pacmanGiantFormDuration() const
	{
		return (int&) __pacmanGiantFormDuration;
	}
	
	inline int &ref_maxCycles() const
	{
		return (int&) __maxCycles;
	}
	

public: // setters

	inline void foodScore(const int &foodScore)
	{
		__foodScore = foodScore;
		has_foodScore(true);
	}
	
	inline void superFoodScore(const int &superFoodScore)
	{
		__superFoodScore = superFoodScore;
		has_superFoodScore(true);
	}
	
	inline void ghostDeathScore(const int &ghostDeathScore)
	{
		__ghostDeathScore = ghostDeathScore;
		has_ghostDeathScore(true);
	}
	
	inline void pacmanDeathScore(const int &pacmanDeathScore)
	{
		__pacmanDeathScore = pacmanDeathScore;
		has_pacmanDeathScore(true);
	}
	
	inline void pacmanGiantFormDuration(const int &pacmanGiantFormDuration)
	{
		__pacmanGiantFormDuration = pacmanGiantFormDuration;
		has_pacmanGiantFormDuration(true);
	}
	
	inline void maxCycles(const int &maxCycles)
	{
		__maxCycles = maxCycles;
		has_maxCycles(true);
	}
	

public: // has_attribute getters

	inline bool has_foodScore() const
	{
		return __has_foodScore;
	}
	
	inline bool has_superFoodScore() const
	{
		return __has_superFoodScore;
	}
	
	inline bool has_ghostDeathScore() const
	{
		return __has_ghostDeathScore;
	}
	
	inline bool has_pacmanDeathScore() const
	{
		return __has_pacmanDeathScore;
	}
	
	inline bool has_pacmanGiantFormDuration() const
	{
		return __has_pacmanGiantFormDuration;
	}
	
	inline bool has_maxCycles() const
	{
		return __has_maxCycles;
	}
	

public: // has_attribute setters

	inline void has_foodScore(const bool &has_foodScore)
	{
		__has_foodScore = has_foodScore;
	}
	
	inline void has_superFoodScore(const bool &has_superFoodScore)
	{
		__has_superFoodScore = has_superFoodScore;
	}
	
	inline void has_ghostDeathScore(const bool &has_ghostDeathScore)
	{
		__has_ghostDeathScore = has_ghostDeathScore;
	}
	
	inline void has_pacmanDeathScore(const bool &has_pacmanDeathScore)
	{
		__has_pacmanDeathScore = has_pacmanDeathScore;
	}
	
	inline void has_pacmanGiantFormDuration(const bool &has_pacmanGiantFormDuration)
	{
		__has_pacmanGiantFormDuration = has_pacmanGiantFormDuration;
	}
	
	inline void has_maxCycles(const bool &has_maxCycles)
	{
		__has_maxCycles = has_maxCycles;
	}
	

public:

	Constants()
	{
		has_foodScore(false);
		has_superFoodScore(false);
		has_ghostDeathScore(false);
		has_pacmanDeathScore(false);
		has_pacmanGiantFormDuration(false);
		has_maxCycles(false);
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
		
		// serialize foodScore
		s += __has_foodScore;
		if (__has_foodScore)
		{
			int tmp1 = __foodScore;
			auto tmp2 = reinterpret_cast<char*>(&tmp1);
			s += std::string(tmp2, sizeof(int));
		}
		
		// serialize superFoodScore
		s += __has_superFoodScore;
		if (__has_superFoodScore)
		{
			int tmp4 = __superFoodScore;
			auto tmp5 = reinterpret_cast<char*>(&tmp4);
			s += std::string(tmp5, sizeof(int));
		}
		
		// serialize ghostDeathScore
		s += __has_ghostDeathScore;
		if (__has_ghostDeathScore)
		{
			int tmp7 = __ghostDeathScore;
			auto tmp8 = reinterpret_cast<char*>(&tmp7);
			s += std::string(tmp8, sizeof(int));
		}
		
		// serialize pacmanDeathScore
		s += __has_pacmanDeathScore;
		if (__has_pacmanDeathScore)
		{
			int tmp10 = __pacmanDeathScore;
			auto tmp11 = reinterpret_cast<char*>(&tmp10);
			s += std::string(tmp11, sizeof(int));
		}
		
		// serialize pacmanGiantFormDuration
		s += __has_pacmanGiantFormDuration;
		if (__has_pacmanGiantFormDuration)
		{
			int tmp13 = __pacmanGiantFormDuration;
			auto tmp14 = reinterpret_cast<char*>(&tmp13);
			s += std::string(tmp14, sizeof(int));
		}
		
		// serialize maxCycles
		s += __has_maxCycles;
		if (__has_maxCycles)
		{
			int tmp16 = __maxCycles;
			auto tmp17 = reinterpret_cast<char*>(&tmp16);
			s += std::string(tmp17, sizeof(int));
		}
		
		return s;
	}
	
	unsigned int deserialize(const std::string &s, unsigned int offset=0)
	{
		// deserialize foodScore
		__has_foodScore = *((unsigned char*) (&s[offset]));
		offset += sizeof(unsigned char);
		if (__has_foodScore)
		{
			__foodScore = *((int*) (&s[offset]));
			offset += sizeof(int);
		}
		
		// deserialize superFoodScore
		__has_superFoodScore = *((unsigned char*) (&s[offset]));
		offset += sizeof(unsigned char);
		if (__has_superFoodScore)
		{
			__superFoodScore = *((int*) (&s[offset]));
			offset += sizeof(int);
		}
		
		// deserialize ghostDeathScore
		__has_ghostDeathScore = *((unsigned char*) (&s[offset]));
		offset += sizeof(unsigned char);
		if (__has_ghostDeathScore)
		{
			__ghostDeathScore = *((int*) (&s[offset]));
			offset += sizeof(int);
		}
		
		// deserialize pacmanDeathScore
		__has_pacmanDeathScore = *((unsigned char*) (&s[offset]));
		offset += sizeof(unsigned char);
		if (__has_pacmanDeathScore)
		{
			__pacmanDeathScore = *((int*) (&s[offset]));
			offset += sizeof(int);
		}
		
		// deserialize pacmanGiantFormDuration
		__has_pacmanGiantFormDuration = *((unsigned char*) (&s[offset]));
		offset += sizeof(unsigned char);
		if (__has_pacmanGiantFormDuration)
		{
			__pacmanGiantFormDuration = *((int*) (&s[offset]));
			offset += sizeof(int);
		}
		
		// deserialize maxCycles
		__has_maxCycles = *((unsigned char*) (&s[offset]));
		offset += sizeof(unsigned char);
		if (__has_maxCycles)
		{
			__maxCycles = *((int*) (&s[offset]));
			offset += sizeof(int);
		}
		
		return offset;
	}
};


class Position : public KSObject
{

protected:

	int __x;
	int __y;

	bool __has_x;
	bool __has_y;


public: // getters

	inline int x() const
	{
		return __x;
	}
	
	inline int y() const
	{
		return __y;
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
	

public: // has_attribute getters

	inline bool has_x() const
	{
		return __has_x;
	}
	
	inline bool has_y() const
	{
		return __has_y;
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
	

public:

	Position()
	{
		has_x(false);
		has_y(false);
	}
	
	static inline const std::string nameStatic()
	{
		return "Position";
	}
	
	virtual inline const std::string name() const
	{
		return "Position";
	}
	
	std::string serialize() const
	{
		std::string s = "";
		
		// serialize x
		s += __has_x;
		if (__has_x)
		{
			int tmp19 = __x;
			auto tmp20 = reinterpret_cast<char*>(&tmp19);
			s += std::string(tmp20, sizeof(int));
		}
		
		// serialize y
		s += __has_y;
		if (__has_y)
		{
			int tmp22 = __y;
			auto tmp23 = reinterpret_cast<char*>(&tmp22);
			s += std::string(tmp23, sizeof(int));
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
		
		return offset;
	}
};


class Agent : public KSObject
{

protected:

	Position __position;
	EDirection __direction;

	bool __has_position;
	bool __has_direction;


public: // getters

	inline Position position() const
	{
		return __position;
	}
	
	inline EDirection direction() const
	{
		return __direction;
	}
	

public: // reference getters

	inline Position &ref_position() const
	{
		return (Position&) __position;
	}
	
	inline EDirection &ref_direction() const
	{
		return (EDirection&) __direction;
	}
	

public: // setters

	inline void position(const Position &position)
	{
		__position = position;
		has_position(true);
	}
	
	inline void direction(const EDirection &direction)
	{
		__direction = direction;
		has_direction(true);
	}
	

public: // has_attribute getters

	inline bool has_position() const
	{
		return __has_position;
	}
	
	inline bool has_direction() const
	{
		return __has_direction;
	}
	

public: // has_attribute setters

	inline void has_position(const bool &has_position)
	{
		__has_position = has_position;
	}
	
	inline void has_direction(const bool &has_direction)
	{
		__has_direction = has_direction;
	}
	

public:

	Agent()
	{
		has_position(false);
		has_direction(false);
	}
	
	static inline const std::string nameStatic()
	{
		return "Agent";
	}
	
	virtual inline const std::string name() const
	{
		return "Agent";
	}
	
	std::string serialize() const
	{
		std::string s = "";
		
		// serialize position
		s += __has_position;
		if (__has_position)
		{
			s += __position.serialize();
		}
		
		// serialize direction
		s += __has_direction;
		if (__has_direction)
		{
			char tmp25 = (char) __direction;
			auto tmp26 = reinterpret_cast<char*>(&tmp25);
			s += std::string(tmp26, sizeof(char));
		}
		
		return s;
	}
	
	unsigned int deserialize(const std::string &s, unsigned int offset=0)
	{
		// deserialize position
		__has_position = *((unsigned char*) (&s[offset]));
		offset += sizeof(unsigned char);
		if (__has_position)
		{
			offset = __position.deserialize(s, offset);
		}
		
		// deserialize direction
		__has_direction = *((unsigned char*) (&s[offset]));
		offset += sizeof(unsigned char);
		if (__has_direction)
		{
			char tmp27;
			tmp27 = *((char*) (&s[offset]));
			offset += sizeof(char);
			__direction = (EDirection) tmp27;
		}
		
		return offset;
	}
};


class Pacman : public Agent
{

protected:

	int __health;
	int __giantFormRemainingTime;

	bool __has_health;
	bool __has_giantFormRemainingTime;


public: // getters

	inline int health() const
	{
		return __health;
	}
	
	inline int giantFormRemainingTime() const
	{
		return __giantFormRemainingTime;
	}
	

public: // reference getters

	inline int &ref_health() const
	{
		return (int&) __health;
	}
	
	inline int &ref_giantFormRemainingTime() const
	{
		return (int&) __giantFormRemainingTime;
	}
	

public: // setters

	inline void health(const int &health)
	{
		__health = health;
		has_health(true);
	}
	
	inline void giantFormRemainingTime(const int &giantFormRemainingTime)
	{
		__giantFormRemainingTime = giantFormRemainingTime;
		has_giantFormRemainingTime(true);
	}
	

public: // has_attribute getters

	inline bool has_health() const
	{
		return __has_health;
	}
	
	inline bool has_giantFormRemainingTime() const
	{
		return __has_giantFormRemainingTime;
	}
	

public: // has_attribute setters

	inline void has_health(const bool &has_health)
	{
		__has_health = has_health;
	}
	
	inline void has_giantFormRemainingTime(const bool &has_giantFormRemainingTime)
	{
		__has_giantFormRemainingTime = has_giantFormRemainingTime;
	}
	

public:

	Pacman()
	{
		has_health(false);
		has_giantFormRemainingTime(false);
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
		
		// serialize parents
		s += Agent::serialize();
		
		// serialize health
		s += __has_health;
		if (__has_health)
		{
			int tmp29 = __health;
			auto tmp30 = reinterpret_cast<char*>(&tmp29);
			s += std::string(tmp30, sizeof(int));
		}
		
		// serialize giantFormRemainingTime
		s += __has_giantFormRemainingTime;
		if (__has_giantFormRemainingTime)
		{
			int tmp32 = __giantFormRemainingTime;
			auto tmp33 = reinterpret_cast<char*>(&tmp32);
			s += std::string(tmp33, sizeof(int));
		}
		
		return s;
	}
	
	unsigned int deserialize(const std::string &s, unsigned int offset=0)
	{
		// deserialize parents
		offset = Agent::deserialize(s, offset);
		
		// deserialize health
		__has_health = *((unsigned char*) (&s[offset]));
		offset += sizeof(unsigned char);
		if (__has_health)
		{
			__health = *((int*) (&s[offset]));
			offset += sizeof(int);
		}
		
		// deserialize giantFormRemainingTime
		__has_giantFormRemainingTime = *((unsigned char*) (&s[offset]));
		offset += sizeof(unsigned char);
		if (__has_giantFormRemainingTime)
		{
			__giantFormRemainingTime = *((int*) (&s[offset]));
			offset += sizeof(int);
		}
		
		return offset;
	}
};


class Ghost : public Agent
{

protected:

	int __id;

	bool __has_id;


public: // getters

	inline int id() const
	{
		return __id;
	}
	

public: // reference getters

	inline int &ref_id() const
	{
		return (int&) __id;
	}
	

public: // setters

	inline void id(const int &id)
	{
		__id = id;
		has_id(true);
	}
	

public: // has_attribute getters

	inline bool has_id() const
	{
		return __has_id;
	}
	

public: // has_attribute setters

	inline void has_id(const bool &has_id)
	{
		__has_id = has_id;
	}
	

public:

	Ghost()
	{
		has_id(false);
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
		
		// serialize parents
		s += Agent::serialize();
		
		// serialize id
		s += __has_id;
		if (__has_id)
		{
			int tmp35 = __id;
			auto tmp36 = reinterpret_cast<char*>(&tmp35);
			s += std::string(tmp36, sizeof(int));
		}
		
		return s;
	}
	
	unsigned int deserialize(const std::string &s, unsigned int offset=0)
	{
		// deserialize parents
		offset = Agent::deserialize(s, offset);
		
		// deserialize id
		__has_id = *((unsigned char*) (&s[offset]));
		offset += sizeof(unsigned char);
		if (__has_id)
		{
			__id = *((int*) (&s[offset]));
			offset += sizeof(int);
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
			int tmp38 = __width;
			auto tmp39 = reinterpret_cast<char*>(&tmp38);
			s += std::string(tmp39, sizeof(int));
		}
		
		// serialize height
		s += __has_height;
		if (__has_height)
		{
			int tmp41 = __height;
			auto tmp42 = reinterpret_cast<char*>(&tmp41);
			s += std::string(tmp42, sizeof(int));
		}
		
		// serialize board
		s += __has_board;
		if (__has_board)
		{
			std::string tmp43 = "";
			unsigned int tmp45 = __board.size();
			auto tmp46 = reinterpret_cast<char*>(&tmp45);
			tmp43 += std::string(tmp46, sizeof(unsigned int));
			while (tmp43.size() && tmp43.back() == 0)
				tmp43.pop_back();
			unsigned char tmp48 = tmp43.size();
			auto tmp49 = reinterpret_cast<char*>(&tmp48);
			s += std::string(tmp49, sizeof(unsigned char));
			s += tmp43;
			
			for (auto &tmp50 : __board)
			{
				s += '\x01';
				std::string tmp51 = "";
				unsigned int tmp53 = tmp50.size();
				auto tmp54 = reinterpret_cast<char*>(&tmp53);
				tmp51 += std::string(tmp54, sizeof(unsigned int));
				while (tmp51.size() && tmp51.back() == 0)
					tmp51.pop_back();
				unsigned char tmp56 = tmp51.size();
				auto tmp57 = reinterpret_cast<char*>(&tmp56);
				s += std::string(tmp57, sizeof(unsigned char));
				s += tmp51;
				
				for (auto &tmp58 : tmp50)
				{
					s += '\x01';
					char tmp60 = (char) tmp58;
					auto tmp61 = reinterpret_cast<char*>(&tmp60);
					s += std::string(tmp61, sizeof(char));
				}
			}
		}
		
		// serialize scores
		s += __has_scores;
		if (__has_scores)
		{
			std::string tmp62 = "";
			unsigned int tmp64 = __scores.size();
			auto tmp65 = reinterpret_cast<char*>(&tmp64);
			tmp62 += std::string(tmp65, sizeof(unsigned int));
			while (tmp62.size() && tmp62.back() == 0)
				tmp62.pop_back();
			unsigned char tmp67 = tmp62.size();
			auto tmp68 = reinterpret_cast<char*>(&tmp67);
			s += std::string(tmp68, sizeof(unsigned char));
			s += tmp62;
			
			for (auto &tmp69 : __scores)
			{
				s += '\x01';
				std::string tmp70 = "";
				unsigned int tmp72 = tmp69.first.size();
				auto tmp73 = reinterpret_cast<char*>(&tmp72);
				tmp70 += std::string(tmp73, sizeof(unsigned int));
				while (tmp70.size() && tmp70.back() == 0)
					tmp70.pop_back();
				unsigned char tmp75 = tmp70.size();
				auto tmp76 = reinterpret_cast<char*>(&tmp75);
				s += std::string(tmp76, sizeof(unsigned char));
				s += tmp70;
				
				s += tmp69.first;
				
				s += '\x01';
				int tmp78 = tmp69.second;
				auto tmp79 = reinterpret_cast<char*>(&tmp78);
				s += std::string(tmp79, sizeof(int));
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
			std::string tmp80 = "";
			unsigned int tmp82 = __ghosts.size();
			auto tmp83 = reinterpret_cast<char*>(&tmp82);
			tmp80 += std::string(tmp83, sizeof(unsigned int));
			while (tmp80.size() && tmp80.back() == 0)
				tmp80.pop_back();
			unsigned char tmp85 = tmp80.size();
			auto tmp86 = reinterpret_cast<char*>(&tmp85);
			s += std::string(tmp86, sizeof(unsigned char));
			s += tmp80;
			
			for (auto &tmp87 : __ghosts)
			{
				s += '\x01';
				s += tmp87.serialize();
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
			unsigned char tmp88;
			tmp88 = *((unsigned char*) (&s[offset]));
			offset += sizeof(unsigned char);
			std::string tmp89 = std::string(&s[offset], tmp88);
			offset += tmp88;
			while (tmp89.size() < sizeof(unsigned int))
				tmp89 += '\x00';
			unsigned int tmp90;
			tmp90 = *((unsigned int*) (&tmp89[0]));
			
			__board.clear();
			for (unsigned int tmp91 = 0; tmp91 < tmp90; tmp91++)
			{
				std::vector<ECell> tmp92;
				offset++;
				unsigned char tmp93;
				tmp93 = *((unsigned char*) (&s[offset]));
				offset += sizeof(unsigned char);
				std::string tmp94 = std::string(&s[offset], tmp93);
				offset += tmp93;
				while (tmp94.size() < sizeof(unsigned int))
					tmp94 += '\x00';
				unsigned int tmp95;
				tmp95 = *((unsigned int*) (&tmp94[0]));
				
				tmp92.clear();
				for (unsigned int tmp96 = 0; tmp96 < tmp95; tmp96++)
				{
					ECell tmp97;
					offset++;
					char tmp98;
					tmp98 = *((char*) (&s[offset]));
					offset += sizeof(char);
					tmp97 = (ECell) tmp98;
					tmp92.push_back(tmp97);
				}
				__board.push_back(tmp92);
			}
		}
		
		// deserialize scores
		__has_scores = *((unsigned char*) (&s[offset]));
		offset += sizeof(unsigned char);
		if (__has_scores)
		{
			unsigned char tmp99;
			tmp99 = *((unsigned char*) (&s[offset]));
			offset += sizeof(unsigned char);
			std::string tmp100 = std::string(&s[offset], tmp99);
			offset += tmp99;
			while (tmp100.size() < sizeof(unsigned int))
				tmp100 += '\x00';
			unsigned int tmp101;
			tmp101 = *((unsigned int*) (&tmp100[0]));
			
			__scores.clear();
			for (unsigned int tmp102 = 0; tmp102 < tmp101; tmp102++)
			{
				std::string tmp103;
				offset++;
				unsigned char tmp105;
				tmp105 = *((unsigned char*) (&s[offset]));
				offset += sizeof(unsigned char);
				std::string tmp106 = std::string(&s[offset], tmp105);
				offset += tmp105;
				while (tmp106.size() < sizeof(unsigned int))
					tmp106 += '\x00';
				unsigned int tmp107;
				tmp107 = *((unsigned int*) (&tmp106[0]));
				
				tmp103 = s.substr(offset, tmp107);
				offset += tmp107;
				
				int tmp104;
				offset++;
				tmp104 = *((int*) (&s[offset]));
				offset += sizeof(int);
				
				__scores[tmp103] = tmp104;
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
			unsigned char tmp108;
			tmp108 = *((unsigned char*) (&s[offset]));
			offset += sizeof(unsigned char);
			std::string tmp109 = std::string(&s[offset], tmp108);
			offset += tmp108;
			while (tmp109.size() < sizeof(unsigned int))
				tmp109 += '\x00';
			unsigned int tmp110;
			tmp110 = *((unsigned int*) (&tmp109[0]));
			
			__ghosts.clear();
			for (unsigned int tmp111 = 0; tmp111 < tmp110; tmp111++)
			{
				Ghost tmp112;
				offset++;
				offset = tmp112.deserialize(s, offset);
				__ghosts.push_back(tmp112);
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
