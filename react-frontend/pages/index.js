import { useQuery } from 'react-query'
import axios from "axios";

export default function Home() {
  const { data } = useQuery('api/titles/series', () => axios("http://127.0.0.1:5000/api/titles/series").then((res) => res.data))

  return (
    <div className='flex flex-wrap bg-gray-200'>
      {data?.map(item => (
        <div className='mx-auto'>
          <div className='w-52 m-5 border-2 border-black rounded-xl overflow-hidden bg-white flex flex-col items-center'>
            <img src={item.images["Poster Art"].url} width={208} />
            <div className='p-5 truncate w-full text-center text-sm'>
              {item.title}
            </div>
          </div>
        </div>
      ))}
    </div>
  )
}
