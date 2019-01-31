#ifndef _KS_COMMANDS_H_
#define _KS_COMMANDS_H_

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


namespace commands
{

enum ECommandDirection
{
	Up = 0,
	Right = 1,
	Down = 2,
	Left = 3,
};


class ChangePacmanDirection : public KSObject
{

protected:

	ECommandDirection __direction;

	bool __has_direction;


public: // getters

	inline ECommandDirection direction() const
	{
		return __direction;
	}
	

public: // reference getters

	inline ECommandDirection &ref_direction() const
	{
		return (ECommandDirection&) __direction;
	}
	

public: // setters

	inline void direction(const ECommandDirection &direction)
	{
		__direction = direction;
		has_direction(true);
	}
	

public: // has_attribute getters

	inline bool has_direction() const
	{
		return __has_direction;
	}
	

public: // has_attribute setters

	inline void has_direction(const bool &has_direction)
	{
		__has_direction = has_direction;
	}
	

public:

	ChangePacmanDirection()
	{
		has_direction(false);
	}
	
	static inline const std::string nameStatic()
	{
		return "ChangePacmanDirection";
	}
	
	virtual inline const std::string name() const
	{
		return "ChangePacmanDirection";
	}
	
	std::string serialize() const
	{
		std::string s = "";
		
		// serialize direction
		s += __has_direction;
		if (__has_direction)
		{
			char tmp1 = (char) __direction;
			auto tmp2 = reinterpret_cast<char*>(&tmp1);
			s += std::string(tmp2, sizeof(char));
		}
		
		return s;
	}
	
	unsigned int deserialize(const std::string &s, unsigned int offset=0)
	{
		// deserialize direction
		__has_direction = *((unsigned char*) (&s[offset]));
		offset += sizeof(unsigned char);
		if (__has_direction)
		{
			char tmp3;
			tmp3 = *((char*) (&s[offset]));
			offset += sizeof(char);
			__direction = (ECommandDirection) tmp3;
		}
		
		return offset;
	}
};


class ChangeGhostDirection : public KSObject
{

protected:

	int __id;
	ECommandDirection __direction;

	bool __has_id;
	bool __has_direction;


public: // getters

	inline int id() const
	{
		return __id;
	}
	
	inline ECommandDirection direction() const
	{
		return __direction;
	}
	

public: // reference getters

	inline int &ref_id() const
	{
		return (int&) __id;
	}
	
	inline ECommandDirection &ref_direction() const
	{
		return (ECommandDirection&) __direction;
	}
	

public: // setters

	inline void id(const int &id)
	{
		__id = id;
		has_id(true);
	}
	
	inline void direction(const ECommandDirection &direction)
	{
		__direction = direction;
		has_direction(true);
	}
	

public: // has_attribute getters

	inline bool has_id() const
	{
		return __has_id;
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
	
	inline void has_direction(const bool &has_direction)
	{
		__has_direction = has_direction;
	}
	

public:

	ChangeGhostDirection()
	{
		has_id(false);
		has_direction(false);
	}
	
	static inline const std::string nameStatic()
	{
		return "ChangeGhostDirection";
	}
	
	virtual inline const std::string name() const
	{
		return "ChangeGhostDirection";
	}
	
	std::string serialize() const
	{
		std::string s = "";
		
		// serialize id
		s += __has_id;
		if (__has_id)
		{
			int tmp5 = __id;
			auto tmp6 = reinterpret_cast<char*>(&tmp5);
			s += std::string(tmp6, sizeof(int));
		}
		
		// serialize direction
		s += __has_direction;
		if (__has_direction)
		{
			char tmp8 = (char) __direction;
			auto tmp9 = reinterpret_cast<char*>(&tmp8);
			s += std::string(tmp9, sizeof(char));
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
		
		// deserialize direction
		__has_direction = *((unsigned char*) (&s[offset]));
		offset += sizeof(unsigned char);
		if (__has_direction)
		{
			char tmp10;
			tmp10 = *((char*) (&s[offset]));
			offset += sizeof(char);
			__direction = (ECommandDirection) tmp10;
		}
		
		return offset;
	}
};

} // namespace commands

} // namespace ks

#endif // _KS_COMMANDS_H_
